'''
Simply draw vertices to screen
'''
import numpy as np

def cood_transfer(camera,point):
    Wx,Wy,Wz = point #world
    world = np.mat([[Wx],[Wy],[Wz],[1]])
    outter = np.zeros((4,4))
    outter[:3,:3] = camera.R
    outter[0,3] = camera.T[0,0]
    outter[1,3] = camera.T[1,0]
    outter[2,3] = camera.T[2,0]
    outter[3,3] = 1.0
    res = camera.get_I() * outter * world
    
    x = res[0,0]
    y = res[1,0]
    z = res[2,0]

    return x,y,z

def naive_vertices_shader(camera,obj,opt):
    camera = camera
    points = obj.v

    points = [cood_transfer(camera,p) for p in points]
    
    opt["vertex_zbuffer"] = [p[2] for p in points]

    points = [(int(p[0]/p[2]),int(p[1]/p[2])) for p in points]

    opt["frame_buffer"] = np.zeros((camera.w,camera.h,3)).astype(int)

    for p in points:
        x = camera.w//2 + p[0]
        y = camera.h//2 + p[1]
        opt["frame_buffer"][x,y] = 255
