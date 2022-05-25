'''
    World cood -> camera cood -> Homogeneous coordinates
'''

import numpy as np

debug = False

def main(camera,obj,opt):
    # vectorize
    T = np.zeros((4,4))
    T[:3,:3] = camera.R
    T[:-1,3:] = camera.T
    T[3,3] = 1 
    pts = np.array(obj.v).T
    pts = np.vstack([pts, np.ones((pts.shape[1]))])
    vertices = T @ pts
    opt["vertex_camera_coods"] = vertices[:-1]

    vertices = camera.I @ vertices
    depth = vertices[2]
    vertices = vertices/depth
    vertices[2] = depth
    vertices += np.mat([camera.w/2, camera.h/2, 0]).T
    
    opt["vertex_screen_coods"] = vertices

    if debug:
        for i in range(8):
            print(vertices[:, i])
            x, y, z = vertices[:, i]
            if z > 1:
                opt['frame_buffer'][int(x[0,0]),int(y[0,0])] = np.array([255,0,0])
            else:
                opt['frame_buffer'][int(x[0,0]),int(y[0,0])] = np.array([0,0,255])
            
    