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
        
        #Rotation, all in Deg, left hand axis
        self.rx = 0
        self.ry = 0
        self.rz = 0

        #Displacement
        self.dx = 0
        self.dy = 0
        self.dz = 0

    