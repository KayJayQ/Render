'''
Check if a pixel is contained by a frag
'''
import numpy as np

color_map = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]


def devide(a,b,c):
    if int(a[1]) == int(b[1]):
        if int(c[1]) > int(a[1]):
            return (a,b,c), None
        elif int(c[1]) < int(a[1]):
            return None, (a,b,c)
    elif int(b[1]) == int(c[1]):
        if int(a[1]) > int(b[1]):
            return (a,b,c), None
        elif int(a[1]) < int(b[1]):
            return None, (a,b,c)
    elif int(c[1]) == int(a[1]):
        if int(b[1]) > int(c[1]):
            return (a,b,c), None
        elif int(b[1]) < int(c[1]):
            return None, (a,b,c)
    p1,mid,p2 = sorted([a,b,c],key=lambda x:x[1])
    lp = lambda y:(p1[0]-p2[0])/(p1[1]-p2[1])*y + p1[0]-p1[1]*(p1[0]-p2[0])/(p1[1]-p2[1])
    p3 = np.array([lp(mid[1]),mid[1]])
    if p2[1] > p1[1]:
        return (p2,mid,p3),(mid,p3,p1)
    else:
        return (p1,mid,p3),(mid,p3,p2)
    return None,None
    


def apex_up(t):
    if t == None:
        return []
    a,b,c = t

    up,r1,r2 = sorted([a,b,c],key=lambda x:-x[1])
    left,right = sorted([r1,r2],key=lambda x:x[0])

    lu = lambda y:(left[0]-up[0])/(left[1]-up[1])*y + left[0]-left[1]*(left[0]-up[0])/(left[1]-up[1])
    ru = lambda y:(right[0]-up[0])/(right[1]-up[1])*y + right[0]-right[1]*(right[0]-up[0])/(right[1]-up[1])

    res = []
    left_most = min([a[0],b[0],c[0]])
    right_most = max([a[0],b[0],c[0]])

    for yc in range(int(left[1]),int(up[1])+1):
        x_l = int(max([lu(yc),left_most]))
        x_r = int(min([ru(yc),right_most]))
        buf = range(x_l,x_r+1)
        res.extend([(x,yc) for x in range(x_l,x_r+1)])

    return res


def apex_down(t):
    if t == None:
        return []
    a,b,c = t
    
    down,r1,r2 = sorted([a,b,c],key=lambda x:x[1])
    left,right = sorted([r1,r2],key=lambda x:x[0])

    ld = lambda y:(left[0]-down[0])/(left[1]-down[1])*y + left[0]-left[1]*(left[0]-down[0])/(left[1]-down[1])
    rd = lambda y:(right[0]-down[0])/(right[1]-down[1])*y + right[0]-right[1]*(right[0]-down[0])/(right[1]-down[1])

    res = []

    left_most = min([a[0],b[0],c[0]])
    right_most = max([a[0],b[0],c[0]])

    for yc in range(int(left[1]),int(down[1])-1,-1):
        x_l = int(max([ld(yc),left_most]))
        x_r = int(min([rd(yc),right_most]))
        buf = range(x_l,x_r+1)
        res.extend([(x,yc) for x in range(x_l,x_r+1)])
        
    return res

def main(camera,obj,opt):
    for i,frag in enumerate(opt["fragments"]):
        a = frag.vertices[0] 
        b = frag.vertices[1]
        c = frag.vertices[2]
        up,down = devide(a,b,c)
        res1 = apex_up(up)
        res2 = apex_down(down)
        for x,y in res1+res2:
            x = int(x) + camera.w//2
            y = int(y) + camera.h//2
            frag.contains.add((x,y))
            print(len(frag.contains))
