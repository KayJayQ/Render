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

        #Geometry Stage
        self.vertice_shader = None # convert world coordinates to camera coordinates 
        self.clipper = None # clip hiden vertices
        self.mapping = None # camera coordinates to screen coordinates

        #Resterization Stage
        self.triangle_setup = None # calculate edge data of each triangle
        self.triangle_traversal = None # traverse each pixel to determine if it is contained by a frag, then give frags output
        self.frag_shader = None # Textureing pixels using UV

        #Blend Stage
        self.template_test = None # not planned to use
        self.depth_test = None # depth test
        self.blend = None # Merge each frag and flush pixel to frame buffer

    def render(camera, obj, opt = dict()):
        self.vertice_shader(camera, obj, opt)
        self.clipper(camera, obj, opt)
        self.mapping(camera, obj, opt)
        self.triangle_setup(camera, obj, opt)
        self.triangle_traversal(camera, obj, opt)
        self.frag_shader(camera, obj, opt)
        #self.template_test(camera, obj, opt)
        self.depth_test(camera, obj, opt)
        self.blend(camera, obj, opt)

