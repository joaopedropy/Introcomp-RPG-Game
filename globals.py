import pygame
from pygame.locals import *


# A janela principal
screen = pygame.display.set_mode((1024, 768))
screen_x, screen_y = screen.get_width(), screen.get_height() 


# Tudo o que for exibido
display = pygame.Surface((screen_x, screen_y)).convert()

# colocar o display na tela
def screen_update():
    screen.blit(display, (0, 0))
    
# escolhas
class Escolhas:
    def __init__(self):
        self.personagem1 = None
        self.personagem2 = None
        self.personagem3 = None
        
escolhas = Escolhas()  # para poderem ser alteradas...

# Algumas cores principais (para facilitar minha vida)
branco = (255, 255, 255)
cinza = (100, 100, 100)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
rosa = (255, 0, 255)