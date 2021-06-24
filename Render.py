from Object import OBJ
import pygame as py
from Window import Window


if __name__ == '__main__':
    print("Start Running...")
    obj = OBJ()
    obj.parse_from_file("D:\\ML\\cube.obj")

    py.init()
    py.display.set_caption("Render")
    screen = py.display.set_mode((800,600))
    window = Window((800,600),screen,obj.name)
    
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.MOUSEBUTTONDOWN:
                print(event.button,"DOWN")
            if event.type == py.MOUSEBUTTONUP:
                print(event.button,"UP")
            if event.type == py.MOUSEMOTION:
                print(event.pos,event.rel)
        window.update()
        window.blitme()

    py.quit()
    quit(0)