from Object import OBJ
import pygame as py
from Window import Window
from Camera import Camera
from Pipeline import Pipeline


if __name__ == '__main__':
    print("Start Running...")
    obj = OBJ()
    obj.parse_from_file("./cube_sample/cube.obj")
    obj.load_texture("./cube_sample/sample.png")

    py.init()
    py.display.set_caption("Render")
    screen = py.display.set_mode((800,600), py.RESIZABLE)
    window = Window((800,600),screen,obj.name)

    camera = Camera("default camera")
    camera.set_resolution(800,600)
    pipeline = Pipeline("alpha")

    window.set_pipeline(pipeline)

    refresh = False
    window.update(camera,obj)
    window.blitme()
    
    while True:

        refresh = False
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == 1:
                    window.rotating = True
                    window.pos = event.pos
                if event.button == 2:
                    window.reset_camera(camera)
                if event.button > 3:
                    window.scale_camera(camera,event.button)
                refresh = True
            if event.type == py.MOUSEBUTTONUP:
                if event.button == 1:
                    window.rotating = False
            if event.type == py.MOUSEMOTION:
                window.rotate_camera(camera,event.rel)
                if window.rotating:
                    refresh = True
            if event.type == py.KEYDOWN:
                if event.key == py.K_w:
                    window.move(camera, [1,0,0])
                if event.key == py.K_s:
                    window.move(camera, [-1,0,0])
                if event.key == py.K_a:
                    window.move(camera, [0,1,0])
                if event.key == py.K_d:
                    window.move(camera, [0,-1,0])
                if event.key == py.K_f:
                    window.move(camera, [0,0,1])
                if event.key == py.K_r:
                    window.move(camera, [0,0,-1])
                refresh = True
        
        if refresh:
            w, h = py.display.get_surface().get_size()
            camera.set_resolution(w, h)
            window.update(camera,obj)
            window.blitme()

    py.quit()
    quit(0)