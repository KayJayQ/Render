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

    def set_pipeline(self,pipeline):
        self.pipeline = pipeline

    def rotate_start(self,x,y):
        self.r_start_x = x
        self.r_start_y = y

    def rotate_end(self,x,y):
        self.r_end_x = x
        self.r_end_y = y

    def rotate_camera(self,camera):
        camera.rotate((self.r_start_x,self.r_start_y),(self.r_end_x,self.r_end_y))


    def update(self):
        self.frame_buffer = self.pipeline.frame_buffer

    def blitme(self):
        #Refresh page
        #draw pixels
        pygame.pixelcopy.array_to_surface(self.screen,self.frame_buffer)
        self.screen.blit(self.TitleText, self.TitleRect)
        pygame.display.flip()
