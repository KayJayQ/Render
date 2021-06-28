import pygame
import numpy as np

class Window:
    '''
    Window of program
    '''

    def __init__(self,resolution,screen, name):
        self.name = name

        self.width,self.height = resolution
        self.screen = screen

        self.frame_buffer = np.zeros((self.width,self.height,3)).astype(int)

        self.screenRect = screen.get_rect()

        self.TitleText = pygame.font.Font('freesansbold.ttf',20).render(f"File: {name}", True, (255,255,255))
        self.TitleRect = self.TitleText.get_rect()
        self.TitleRect.center = (self.width//2,15)

        self.rotating = False
        self.update_screen = True

    def set_pipeline(self,pipeline):
        self.pipeline = pipeline

    def rotate_camera(self,camera,rel):
        if not self.rotating:
            return
        cur_x,cur_y = self.pos
        m_x,m_y = rel
        camera.rotate((cur_x,cur_y),(cur_x + m_x, cur_y + m_y))
        self.pos = (cur_x + m_x, cur_y + m_y)
        self.update_screen = True


    def reset_camera(self,camera):
        camera.reset()
        self.update_screen = True

    def scale_camera(self,camera,direction):
        if direction == 4:
            camera.scale_up()
        if direction == 5:
            camera.scale_down()
        self.update_screen = True



    def update(self,camera,obj):
        if self.update_screen:
            self.pipeline.render(camera,obj,dict())
            self.update_screen = False
        self.frame_buffer = self.pipeline.frame_buffer
        

    def blitme(self):
        #Refresh page
        #draw pixels
        pygame.pixelcopy.array_to_surface(self.screen,self.frame_buffer)
        self.screen.blit(self.TitleText, self.TitleRect)
        pygame.display.flip()
