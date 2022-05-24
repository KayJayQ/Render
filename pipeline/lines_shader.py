
'''
    Draw lines on screen
'''

import numpy as np

debug = True



def test_vertex(v):
    x,y,z = v
    if x < 0 or y < 0:
        return False
    if x >= w or y >= h:
        return False
    if z < 0:
        return False
    return True

class LineFrag:

    lineColor = np.array([255, 255, 255])

    def __init__(self, start, end):
        if test_vertex(start):
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start
            
        self.restorization()

    def restorization(self):
        x0,y0,z0 = self.start
        x1,y1,z1 = self.end
        x0 = int(x0[0,0])
        x1 = int(x1[0,0])
        y0 = int(y0[0,0])
        y1 = int(y1[0,0])
        z0 = (z0[0,0])
        z1 = (z1[0,0])
        

        if np.abs(x0-x1) > np.abs(y0-y1):
            self.frag = np.zeros((3,np.abs(x0-x1+1)))
            self.frag[0,:] = np.linspace(x0, x1, np.abs(x0-x1+1))
            self.frag[1,:] = np.linspace(y0, y1, np.abs(x0-x1+1))
            self.frag[2:,] = np.linspace(z0, z1, np.abs(x0-x1+1))
        else:
            self.frag = np.zeros((3,np.abs(y0-y1+1)))
            self.frag[1,:] = np.linspace(y0, y1, np.abs(y0-y1+1))
            self.frag[0,:] = np.linspace(x0, x1, np.abs(y0-y1+1))
            self.frag[2:,] = np.linspace(z0, z1, np.abs(y0-y1+1))
         
        cood = self.frag

        x = cood[0].astype(int)
        y = cood[1].astype(int)
        z = cood[2]

        xlim = np.where((x > 0) & (x < w))
        x = x[xlim]
        y = y[xlim]
        z = z[xlim]
        ylim = np.where((y>0)&(y<h))
        x = x[ylim]
        y = y[ylim]
        z = z[ylim]

        self.frag = np.array([x,y,z])
         

        

def main(camera,obj,opt):
    global w
    global h
    w = camera.w
    h = camera.h
    lines = dict()
    vertex = opt['vertex_screen_coods']
    for face in obj.f:
        a,b,c = face['v']
        a, b, c = sorted([a,b,c])
        if a in lines.keys():
            lines[a].add(b)
            lines[a].add(c)
        else:
            lines[a] = set([b,c])
        if b in lines.keys():
            lines[b].add(c)
        else:
            lines[b] = set([c])

    line_list = []
    for start,ends in lines.items():
        for end in ends:
            if test_vertex(vertex[:, start-1]) or test_vertex(vertex[:, end-1]):
                line_list.append([start, end])

    lines = []
    for line in line_list:
        start, end = line
        lines.append(LineFrag(vertex[:, start-1], vertex[:, end-1]))     

    opt["line_frags"] = lines

    if debug:
        for line in lines:
            x, y = line.frag[:2].astype(int)
            opt["frame_buffer"][x, y] = LineFrag.lineColor
