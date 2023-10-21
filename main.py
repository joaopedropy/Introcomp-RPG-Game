import pygame
from pygame.locals import *
from globals import *
from funções.functions import button, write
# from impmusicas import *

pygame.init()

class Main:
    def __init__(self):
        
        self.running = True
        self.background = pygame.image.load("backgrounds/main menu background.png").convert()
        self.start()
        
    def start(self):
        while self.running:
            
            window.start(bg = self.background)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    pass
                    
                    
            pygame.display.flip()
            
Main()