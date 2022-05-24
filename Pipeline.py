import numpy as np

from pipeline import vertices_shader
from pipeline import lines_shader

def placeholder(camera,obj,opt):
    pass

class Pipeline():
    '''
    Render pipeline
    Input: OBJ object
    Output: Pixel Array Map
    Fully customized

    Callable render method:
    func(camera, obj, opt) opt for optional parameters, dict() type, empty dict() for default
    '''

    def __init__(self, name):
        self.name = name

        self.camera = None #Camera object, including fx,fy,u0,v0,R,T and screen resolution

        #Step processor(camera, obj) processed result will be stored at origin OBJ object

        self.components = [vertices_shader.main,
                           lines_shader.main]

        #final frame buffer
        self.frame_buffer = None

    def render(self,camera, obj, opt = dict()):
        opt["frame_buffer"] = np.zeros((camera.w,camera.h,3)).astype(int)
        
        for component in self.components:
            component(camera, obj, opt)

        #print(opt)
        self.frame_buffer = opt["frame_buffer"]

