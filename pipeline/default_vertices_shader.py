
'''
World cood -> camera cood
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
    res = camera.get_I()*outter * world
    
    x = res[0,0]
    y = res[1,0]
    z = res[2,0]

    return x,y,z

def main(camera,obj,opt):
    points = obj.v

    points = [cood_transfer(camera,p) for p in points]
    
    opt["vertices_in_camera_cood"] = points
