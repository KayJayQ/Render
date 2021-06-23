class OBJ:
    '''
        Object files

        No group allowed

        supported title:
            #
            mtllib
            usemtl
            o
            v
            vt
            vn
            f

    '''

    def __init__(self):
        self.name = "New Object"

        self.v = []
        self.vt = []
        self.vn = []
        self.f = []

        self.mtllib = dict() # materials lib
        self.mtl = None # materials of object

    def parse_from_file(file):
        with open(file,'r') as f:
            pass
