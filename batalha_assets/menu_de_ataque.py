import pygame
from funções.functions import button, write
from globals import *


class Frame:
    
    def __init__(self):
        
        # Menu de ataque  ( apenas o campo )
        self.menuframe = pygame.Rect(0, 0, screen_x / 1.8, screen_y // 3.5)
        self.menuframe.center = (screen_x // 3.3, screen_y // 1.2)
        
        # Menu de informações ( apenas o campo )
        self.informationframe = pygame.Rect(0, 0, screen_x / 2.6, screen_y // 3.5)
        self.informationframe.center = (screen_x // 1.28, screen_y // 1.2)


class MenuDeEscolha(Frame):
    
    def __init__(self, atual, active = False):
        super().__init__()
        
        self.ataque1 = button((self.menuframe.topleft[0] + 140, self.menuframe.topleft[1] + 60), (250, 80), (200, 200, 200), nome = "ataque1")
        self.ataque2 = button((self.menuframe.topright[0] - 140, self.menuframe.topleft[1] + 60), (250, 80), (200, 200, 200), nome = "ataque2")
        self.defesa = button((self.menuframe.topleft[0] + 140, self.menuframe.topleft[1] + 160), (250, 80), (200, 200, 200), nome = "defesa")
        self.botoes = [self.ataque1, self.ataque2, self.defesa]
        self.atual = atual
        
    def update(self):
        
                    # Menu de escolha de ataque
            pygame.draw.rect(display, cinza, self.menuframe, 0, 15), pygame.draw.rect(display, preto, self.menuframe, 2, 15)
            pygame.draw.rect(display, cinza, self.informationframe, 0, 15), pygame.draw.rect(display, preto, self.informationframe, 2, 15)
        
        # Atualizar o menu de ataque
            self.ataque1.update(rounded_edge=20)
            self.ataque2.update(rounded_edge=20)
            self.defesa.update(rounded_edge=20)
            
            # Escrever cada coisa
            write(f"{self.atual.nome}", (self.informationframe.midtop[0], self.informationframe.midtop[1] + 50), 50, (200, 200, 200))
            write(f"Ataque", self.ataque1.rect.center, 25, (0, 0, 0))
            write(f"{self.atual.ataqueEspecial}", self.ataque2.rect.center, 25, (0, 0, 0))
            write(f"Defesa", self.defesa.rect.center, 25, (0, 0, 0))
            

class MenuDeAtaque(Frame):
    
    def __init__(self, inimigos):
        super().__init__()
        
        self.inimigos = inimigos
        self.inimigo1 = button((self.menuframe.topleft[0] + 140, self.menuframe.topleft[1] + 60), (250, 80), (200, 200, 200), nome=self.inimigos[0].nome)
        self.inimigo2 = button((self.menuframe.topright[0] - 140, self.menuframe.topright[1] + 60), (250, 80), (200, 200, 200), nome=self.inimigos[1].nome)
        self.inimigo3 = button((self.menuframe.topleft[0] + 140, self.menuframe.topleft[1] + 160), (250, 80), (200, 200, 200), nome=self.inimigos[2].nome)
        self.botoes = [self.inimigo1, self.inimigo2, self.inimigo3]
        self.escolha = None
        
    def update(self):
        
        # Menu de escolha de ataque
        pygame.draw.rect(display, cinza, self.menuframe, 0, 15), pygame.draw.rect(display, preto, self.menuframe, 2, 15)
        pygame.draw.rect(display, cinza, self.informationframe, 0, 15), pygame.draw.rect(display, preto, self.informationframe, 2, 15)
        
        self.inimigo1.update(rounded_edge=20)
        self.inimigo2.update(rounded_edge=20)
        self.inimigo3.update(rounded_edge=20)
        
        # write(f"{self.atual.nome}", (self.informationframe.midtop[0], self.informationframe.midtop[1] + 50), 50, (200, 200, 200))
        write(f"{self.inimigos[0].nome}", self.inimigo1.rect.center, 25, (0, 0, 0))
        write(f"{self.inimigos[1].nome}", self.inimigo2.rect.center, 25, (0, 0, 0))
        write(f"{self.inimigos[2].nome}", self.inimigo3.rect.center, 25, (0, 0, 0))