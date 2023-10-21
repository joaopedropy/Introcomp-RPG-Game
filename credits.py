import pygame
from pygame.locals import *
from globals import window, cores
from musiccontrol import radio
from funções.functions import Button, write


class Credits:
    def __init__(self):
        
        self.running = True
        radio.stop()
        radio.play("musicas/Seleção.wav")
        self.background = pygame.image.load("backgrounds/creditosbg.png")
        
        while self.running:
            window.start(bg = self.background)
            self.draw()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    radio.play("musicas/Menu.wav")
                    
            pygame.display.update()
            
    def draw(self):
        
        write("Desenvolvido por:", (window.rect.centerx, window.rect.centery - 250), 50, (255, 255, 0))
        write("Wendell Kauã Ribeiro Ribet Loureiro", (window.rect.centerx, window.rect.centery - 150), 50, (255, 255, 255))
        write("João Pedro Pina Coelho", (window.rect.centerx, window.rect.centery - 100), 50, (255, 255, 255))
        write("Com a ajuda de:", (window.rect.centerx, window.rect.centery + 50), 50, (255, 255, 0))
        write("Deus", (window.rect.centerx, window.rect.centery + 150), 50, (255, 255, 255))
        write("Chat GPT", (window.rect.centerx, window.rect.centery + 200), 50, (255, 255, 255))
        
        write("Pressione X para voltar", (window.rect.centerx, window.rect.centery + 300), 35, (255, 255, 255))