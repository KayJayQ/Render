import numpy as np

class Camera:
    '''
    Camera Class
    '''

    def __init__(self, name):
        self.name = name

        #Resulution
        self.w = 800
        self.h = 600
        
        #Rotation of world, all in Deg, right hand axis
        self.rx = 0
        self.ry = 0
        self.rz = 0

        #Displacement of world center
        self.cx = 0
        self.cy = 0
        self.cz = 0

        #Displacement of camera
        self.dx = 0
        self.dy = 0
        self.dz = 0

    def rotate(self,rel):
        #max 5
        rel_x, rel_y = rel
        if abs(rel_x) > 5:
            rel_x = max([-5,rel_x])
            rel_x = min([5,rel_x])
        if abs(rel_y) > 5:
            rel_y = max([-5,rel_y])
            rel_y = min([5,rel_y])
        
        rel_map = lambda x:x*2


    def user_parameters(self):
        #return readable parameters
        s = f'''
        Camera Parameters (readable)
        Resolution: ({self.w},{self.h})
        Rotation (deg): Rx {self.rx},Ry {self.ry},Rz {self.rz}
        World Displacement: Dx {self.cx},Dy {self.cy},Dz {self.cz}
        Camera Displacement: Dx {self.dx},Dy {self.dy},Dz {self.dz}
        '''
        return s
    