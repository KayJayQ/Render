from Object import OBJ
import pygame as py
from Window import Window
from Camera import Camera
from Pipeline import Pipeline

from pipeline import naive_vertice_shader


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
    pipeline.vertice_shader = naive_vertice_shader.naive_vertices_shader
    
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == 1:
                    window.rotate_start(event.pos[0],event.pos[1])
            if event.type == py.MOUSEBUTTONUP:
                if event.button == 1:
                    window.rotate_end(event.pos[0],event.pos[1])
                    window.rotate_camera(camera)
            if event.type == py.MOUSEMOTION:
                pass
        pipeline.render(camera,obj,dict())
        window.update()
        window.blitme()

    py.quit()
    quit(0)