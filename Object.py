import numpy as np
from matplotlib import pyplot as plt

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

        self.mtllib = None # materials lib
        self.mtl = None # materials of object

        # since ray tracing is not implemented,
        # use texture file directly
        self.texture = None

    def load_texture(self, path):
        self.texture = plt.imread(path)
        assert len(self.texture.shape) == 3 and self.texture.shape[2] in [3,4], "Texture format error"

    def parse_from_file(self,file):
        with open(file,'r') as f:
            for line in f:
                line = line.rstrip()
                if '#' in line:
                    continue
                if len(line) < 2:
                    continue

                header = line.split()[0]
                if header == 'o':
                    self.name = line.split()[1]
                elif header == 'v':
                    #vertice
                    x,y,z = map(float,line.split()[1:])
                    self.v.append((x,y,z))
                elif header == 'vt':
                    #texture vertice
                    x,y = map(float,line.split()[1:])
                    self.vt.append((x,y))
                elif header == 'vn':
                    #vertice normal
                    x,y,z = map(float,line.split()[1:])
                    self.vn.append((x,y,z))
                elif header == 'f':
                    #face
                    frags = line.split()[1:]
                    face = dict()
                    face['v'] = [int(i.split('/')[0]) for i in frags]
                    face['t'] = [int(i.split('/')[1]) for i in frags]
                    face['n'] = [int(i.split('/')[2]) for i in frags]
                    self.f.append(face)
    
    def __str__(self):
        return f"Object: {self.name}\n v: {self.v}\n vt: {self.vt}\n vn:{self.vn}\n f:{self.f}"
                
