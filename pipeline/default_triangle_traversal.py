'''
Check if a pixel is contained by a frag
'''
import numpy as np

color_map = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]


def inside(pa,pb,pc):
    t1 = pa[0] * pb[1] - pb[0] * pa[1]
    t2 = pb[0] * pc[1] - pc[0] * pb[1]
    t3 = pc[0] * pa[1] - pa[0] * pc[1]
    return np.sign(t1) == np.sign(t2) == np.sign(t3)

def sampling_fill(x,y,sampling):
    if sampling == 1:
        return [(x,y)]
    res = []
    for i in range(sampling):
        res.append((x+i,y+i))
    return res

def main(camera,obj,opt):
    sampling = 1
    for i,frag in enumerate(opt["fragments"]):
        x_min = int(min([x for x,y in frag.vertices]))
        x_max = int(max([x for x,y in frag.vertices]))
        y_min = int(min([y for x,y in frag.vertices]))
        y_max = int(max([y for x,y in frag.vertices]))
        a = frag.vertices[0] 
        b = frag.vertices[1]
        c = frag.vertices[2]
        for x in range(x_min,x_max,sampling):
            for y in range(y_min,y_max,sampling):
                p = [x,y]
                pa = [a[0]-p[0],a[1]-p[1]]
                pb = [b[0]-p[0],b[1]-p[1]]
                pc = [c[0]-p[0],c[1]-p[1]]
                if inside(pa,pb,pc):
                    sx = x + camera.w//2
                    sy = y + camera.h//2
                    pixels = sampling_fill(sx,sy,sampling)
                    for pixel in pixels:
                        frag.contains.add(pixel)
                        opt['frame_buffer'][pixel[0],pixel[1]] = color_map[i%6]

