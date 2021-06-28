'''
Calculate edge of each triangle, create Fragement
'''
import numpy as np

class Fragement:
    '''
    Render fragment, includes everything of a triangle face
    '''

    def __init__(self):
        self.vertices = []
        self.depths = []
        self.normals = []
        self.UV = []
        self.contains = set() #if a pixel is contianed by frag  {(800,600),(801,601)}
        self.pixels = dict() #pixel dictionary. self.pixels[800][600] = (255,255,0,1)
        self.depth_buffer = dict() #depth buffer of each pixel.  self.depth_buffer[800][600] = 3.0

def main(camera,obj,opt):
    faces = obj.f
    frags = []
    for face in faces:
        frag = Fragement()
        frag.vertices.extend([list(opt['vertices_in_camera_cood'][i-1][:-1]) for i in face['v']])
        frag.depths.extend([opt['vertices_in_camera_cood'][i-1][-1] for i in face['v']])
        #utilize to screen here
        for i in range(3):
            frag.vertices[i][0] /= frag.depths[i]
            frag.vertices[i][1] /= frag.depths[i]
        frag.normals.extend([obj.vn[i-1] for i in face['n']])
        frag.UV.extend([obj.vt[i-1] for i in face['t']])
        frags.append(frag)
    opt['fragments'] = frags


    
    


