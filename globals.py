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

class Cores:
    def __init__(self):
        
        self.azul_escuro = (7, 0, 77)
        self.azul_claro = (33, 118, 255)
        self.azul_esverdeado = (36, 95, 89)
        self.vinho = (112, 22, 30)
        self.verde_claro = (156, 227, 125)
        
cores = Cores()

class Escolhas:
    def __init__(self):
        self.escolha1 = ""
        self.escolha2 = ""
        self.escolha3 = ""
        
escolhas = Escolhas()