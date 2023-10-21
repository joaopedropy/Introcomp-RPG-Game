import pygame
from pygame.locals import *


# A janela principal
class Window:
    def __init__(self):
        
        self.largura = 1024
        self.altura = 768
        self.screen = pygame.display.set_mode((self.largura, self.altura))
        self.screen_color = (0, 0, 0)
        self.display = pygame.Surface((self.largura, self.altura)).convert()
        self.display_color = (0, 0, 0)
        self.rect = self.display.get_rect()
        
    def start(self, bg = pygame.Surface((1024, 768))):
        
        self.screen.fill(self.screen_color)
        self.screen.blit(self.display, (0, 0))
        self.display.fill(self.display_color)
        self.display.blit(bg, (0, 0))

window = Window()

