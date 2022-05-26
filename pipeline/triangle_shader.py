
'''
    Test normal of frags and restorize valid frags.
'''

import numpy as np

debug = True

class Frag:

    Color = np.array([255,0,0])
    '''
    Vertices: vertices from vertices shader (Screen cood and with depth buffer)
    Textures: UV coods
    Normals: origin normal of vertices
    '''
    def __init__(self, vertices, textures):
        self.p = np.array(vertices)
        self.uv = np.array(textures)

    def limit(self, n, floor, ceil):
        if n >= floor and n <= ceil:
            return n
        if n > ceil:
            return ceil
        return floor

    def rasterization(self):
        x_min = int(self.p[:,0].min())
        x_max = int(self.p[:,0].max())
        y_min = int(self.p[:,1].min())
        y_max = int(self.p[:,1].max())

        x_min = self.limit(x_min, 0, W-1)
        x_max = self.limit(x_max, 0, W-1)
        y_min = self.limit(y_min, 0, H-1)
        y_max = self.limit(y_max, 0, H-1)

        P = np.mgrid[x_min:x_max, y_min:y_max].T.reshape((-1,2))

        P0P2 = self.p[2,:-1] - self.p[0,:-1]
        P2P1 = self.p[1,:-1] - self.p[2,:-1]
        P1P0 = self.p[0,:-1] - self.p[1,:-1]

        P0P = P - self.p[0,:-1]
        P1P = P - self.p[1,:-1]
        P2P = P - self.p[2,:-1]

        t1 = P0P2[0] * P0P[:,1] - P0P[:,0] * P0P2[1]
        t2 = P2P1[0] * P2P[:,1] - P2P[:,0] * P2P1[1]
        t3 = P1P0[0] * P1P[:,1] - P1P[:,0] * P1P0[1]

        self.pixels = P[np.where((t1 > 0) & (t2 > 0) & (t3 > 0))]

        P0P = self.pixels - self.p[0,:-1]
        P1P = self.pixels - self.p[1,:-1]
        P2P = self.pixels - self.p[2,:-1]

        n = len(self.pixels)

        vx = np.vstack([-1*np.ones(n) * P1P0[0], np.ones(n) * P0P2[0], -P0P[:,0]]).T
        vy = np.vstack([-1*np.ones(n) * P1P0[1], np.ones(n) * P0P2[1], -P0P[:,1]]).T

        res = np.cross(vx, vy)
        b = res[:,0] / res[:,2]
        c = res[:,1] / res[:,2]
        a = 1 - b - c

        depth = self.p[:,-1]
        d0, d1, d2 = depth
        self.depths = a * depth[0] + b * depth[1] + c * depth[2]
        uv0 = a * self.uv[0,0] / d0 + b * self.uv[1,0] / d1 + c * self.uv[2,0] / d2
        uv1 = a * self.uv[0,1] / d0 + b * self.uv[1,1] / d1 + c * self.uv[2,1] / d2
        duv = a / d0 + b / d1 + c / d2

        self.uvs = np.vstack([uv0/duv,uv1/duv]).T
               
# simple depth pre test
def test_depths(vertices):
    depths = vertices[:,-1]
    d0,d1,d2 = depths
    return d0 > 0 or d1 > 0 or d2 > 0

def test_normal(normals):
    n0, n1, n2 = normals
    normal = n0 + n1 + n2
    normal = np.matrix(normal).T
    z = (R@normal).T*(T)
    return z < 0


def main(camera,obj,opt):
    textures = np.array(obj.vt).T
    normals = np.array(obj.vn).T
    global R
    global T
    R = camera.R
    T = camera.T
    global W
    global H 
    W = camera.w 
    H = camera.h 

    frags = []

    for face in obj.f:
        v = np.array(face['v']) - 1
        v = opt['vertex_screen_coods'][:,v]
        if not test_depths(v.T):
            continue
        uv = np.array(face['t']) - 1
        uv = textures[:,uv]
        n = np.array(face['n']) - 1
        n = normals[:,n]
        if test_normal(n.T):
            V = opt['vertex_camera_coods']
            frag = Frag(v.T, uv.T)
            frag.rasterization()
            frags.append(frag)

    opt['frag_setups'] = frags
    
    if debug:
        count = 0
        for frag in frags:
            if len(frag.pixels) > 0:
                count += 1
                x, y = frag.pixels.T.astype(int)
                uvx, uvy = frag.uvs.T
                h, w = obj.texture.shape[:-1]
                uvx = (uvx * w).astype(int)*-1
                uvy = (uvy * h).astype(int)
                uvx[uvx >= w] = w - 1
                uvy[uvy >= h] = h - 1
                uvx[uvx < -w] = -w
                uvy[uvy < -h] = -h
                colormap = (obj.texture[uvy, uvx, :-1] * 255).astype(int)
                x[x >= camera.w] = camera.w - 1
                y[y >= camera.h] = camera.h - 1
                opt["frame_buffer"][x, y] = colormap
        print(count, "frags were rendered")


