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


    def update(self):
        pass

    def blitme(self):
        #Refresh page
        #draw pixels
        pygame.pixelcopy.array_to_surface(self.screen,self.frame_buffer)
        self.screen.blit(self.TitleText, self.TitleRect)
        pygame.display.flip()
