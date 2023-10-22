import pygame
from pygame.locals import *
from globals import window, cores
from musicas.musiccontrol import radio
from funções.functions import Button, write


class Credits:
    def __init__(self):
        
        self.running = True # define a condição de loop
        
        radio.stop() # para a música anterior
        radio.play("musicas/Créditos.mp3") # inicia uma nova música
        
        self.background = pygame.image.load("backgrounds/creditosbg.png") # Carrega o background

        self.start() # inicia o loop principal
        
    def start(self): # função do loop
        while self.running:
            
            window.start(bg = self.background) # iniciar tela
            self.draw() # desenhar tudo o que deve ser desenhado
            
            for event in pygame.event.get(): # eventos
                if event.type == QUIT: 
                    self.exit()
                if event.type == KEYDOWN: # teclas do teclado pressionadas
                    if event.key == K_x: self.exit() # sair desta tela
                                            
            pygame.display.update()
            
    def draw(self):  # Tudo o que será desenhado no loop
        
        write("Desenvolvido por:", (window.rect.centerx, window.rect.centery - 250), 50, (255, 255, 0))
        write("Wendell Kauã Ribeiro Ribet Loureiro", (window.rect.centerx, window.rect.centery - 150), 50, (255, 255, 255))
        write("João Pedro Pina Coelho", (window.rect.centerx, window.rect.centery - 100), 50, (255, 255, 255))
        write("Com a ajuda de:", (window.rect.centerx, window.rect.centery + 50), 50, (255, 255, 0))
        write("Deus", (window.rect.centerx, window.rect.centery + 150), 50, (255, 255, 255))
        write("Chat GPT", (window.rect.centerx, window.rect.centery + 200), 50, (255, 255, 255))
        
        write("Pressione X para voltar", (window.rect.centerx, window.rect.centery + 300), 35, (255, 255, 255))
         
    def exit(self): # funçao para sair 
        
        # sair: sair desta tela; parar música e começar música do menu
        self.running = False
        radio.play("musicas/Menu.wav")