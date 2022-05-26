import numpy as np

def get_R(x,y,z):
    x = x / 180 * np.pi
    y = y / 180 * np.pi
    z = z / 180 * np.pi
    Rx = np.mat([[1,0,0],[0,np.cos(x),-np.sin(x)],[0,np.sin(x),np.cos(x)]])
    Ry = np.mat([[np.cos(y),0,np.sin(y)],[0,1,0],[-np.sin(y),0,np.cos(y)]])
    Rz = np.mat([[np.cos(z),-np.sin(z),0],[np.sin(z),np.cos(z),0],[0,0,1]])
    return Rx*Ry*Rz

class Camera:
    '''
    Camera Class
    '''
    buffer_weight = 200
    buffer_height = 200

    def __init__(self, name):
        self.name = name

        #Resulution
        self.w = 800
        self.h = 600

        #Displacement of world center
        self.cx = 0.0
        self.cy = 0.0
        self.cz = 0.0

        #Displacement of camera
        self.dx = 0.0
        self.dy = 0.0
        self.dz = 2.0

        #Camera inner paramters
        self.fx = 80
        self.fy = 80
        self.u0 = 0
        self.v0 = 0

        self.I = np.mat([[self.fx,0,self.u0,0],[0,self.fy,self.v0,0],[0,0,1,0]])


        #Origin Matrix
        self.R = get_R(0,0,0)
        self.T = np.mat([[0.0],[0.0],[10.0]])

    def set_resolution(self, w, h):
        self.w = w + Camera.buffer_weight
        self.h = h + Camera.buffer_height

    def reset(self):
        self.R = get_R(0,0,0)
        self.T = np.mat([[0.],[0.],[10.]])
        self.fx = 80
        self.fy = 80

    def move(self, x, y, z):
        factor = (-1/self.fx)*10
        T = np.mat([[x*factor], [y*factor], [z*factor]]).astype(np.float)
        self.T += T

    def rotate(self,init,end):

        x0,y0 = init
        x1,y1 = end

        #Reflect screen axis cood to [-1,1]
        x1,x0 = map(lambda x:x*2/self.w-1.0,(x0,x1))
        y1,y0 = map(lambda x:x*2/self.h-1.0,(y0,y1))

        #Convert 2d cood to on sphere 3d cood
        dist0 = x0**2 + y0**2
        if dist0 < 1.0:
            z0 = (1-dist0)**0.5
        else:
            x0 = x0 / dist0**0.5
            y0 = y0 / dist0**0.5
            z0 = 0.0
        dist1 = x1**2 + y1**2
        if dist1 < 1.0:
            z1 = (1-dist1)**0.5
        else:
            x1 = x1 / dist1**0.5
            y1 = y1 / dist1**0.5
            z1 = 0.0
        
        #Get rotation angel
        vec0 = np.array([x0,y0,z0])
        vec1 = np.array([x1,y1,z1])
        theta = np.arccos(np.dot(vec0,vec1))
        U = np.cross(vec0,vec1)
        U_m = np.linalg.norm(U)
        U = U/U_m

        ux,uy,uz = U
        cos = np.cos(theta)
        sin = np.sin(theta)

        trans_R = np.mat([[cos+ux**2*(1-cos), ux*uy*(1-cos)-uz*sin, ux*uz*(1-cos)+uy*sin],
                            [uy*ux*(1-cos)+uz*sin, cos+uy**2*(1-cos), uy*uz*(1-cos)-ux*sin],
                            [uz*ux*(1-cos)-uy*sin, uz*uy*(1-cos)+ux*sin, cos+uz**2*(1-cos)]])
        if U_m < 1e-4:  
            trans_R = np.mat([[1,0,0],[0,1,0],[0,0,1]])
        
        #Update current rotation matrix
        self.R = self.R * trans_R

    def scale_up(self):
        self.fx = self.fx//2
        self.fy = self.fy//2
        self.I = np.mat([[self.fx,0,self.u0,0],[0,self.fy,self.v0,0],[0,0,1,0]])

    def scale_down(self):
        self.fx = self.fx * 2
        self.fy = self.fy * 2
        self.I = np.mat([[self.fx,0,self.u0,0],[0,self.fy,self.v0,0],[0,0,1,0]])
