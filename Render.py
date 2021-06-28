from Object import OBJ
import pygame as py
from Window import Window
from Camera import Camera
from Pipeline import Pipeline

from pipeline import default_vertices_shader
from pipeline import default_triangle_setup
from pipeline import default_triangle_traversal


if __name__ == '__main__':
    print("Start Running...")
    obj = OBJ()
    obj.parse_from_file("./cube.obj")

    py.init()
    py.display.set_caption("Render")
    screen = py.display.set_mode((800,600))
    window = Window((800,600),screen,obj.name)

    camera = Camera("default camera")
    pipeline = Pipeline("naive")

    window.set_pipeline(pipeline)
    pipeline.vertice_shader = default_vertices_shader.main
    pipeline.triangle_setup = default_triangle_setup.main
    pipeline.triangle_traversal = default_triangle_traversal.main

    
    while True:
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
            if event.type == py.MOUSEBUTTONUP:
                if event.button == 1:
                    window.rotating = False
            if event.type == py.MOUSEMOTION:
                window.rotate_camera(camera,event.rel)
        
        window.update(camera,obj)
        window.blitme()

    py.quit()
    quit(0)