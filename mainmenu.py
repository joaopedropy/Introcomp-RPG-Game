import pygame
from pygame.locals import *
from globals import window, cores
from funções.functions import Button
from musiccontrol import radio
from credits import Credits


pygame.init()


class Main: # a classe principal do menu
    def __init__(self):
        
        radio.play("musicas/Menu.wav")
        self.running = True # define que o menu está ativo
        self.background = pygame.image.load("backgrounds/mainmenubg.png").convert() # Plano de fundo
        self.posicao_da_escolha = 0
        
        self.start_button = Button(
            pos = (-15, window.rect.centery),
            size = (300, 60),
            color = cores.verde_claro,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            anchor="left",
            text = "Play",
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        
        self.credits_button = Button(
            pos = (-15, window.rect.centery + 120),
            size = (300, 60),
            color = cores.verde_claro,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            anchor="left",
            text = "Credits",
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        
        self.quit_button = Button(
            pos = (-15, window.rect.centery + 240),
            size = (300, 60),
            color = cores.verde_claro,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            anchor="left",
            text = "Quit",
            text_color=cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        
        
        self.buttons = [
            self.quit_button,
            self.credits_button,
            self.start_button
        ]
        
    
    def drawings(self):
        
        self.start_button.show()
        self.credits_button.show()
        self.quit_button.show()
        
    def start(self):
        while self.running:
            
            window.start(bg = self.background) # inicia a tela e coloca o plano de fundo
            self.drawings()
            
            for event in pygame.event.get(): # Eventos
                if event.type == QUIT:
                    pygame.quit()
                    
                if event.type == KEYDOWN: # atualiza posição da escolha
                    if event.key == K_UP: self.posicao_da_escolha += 1
                    if event.key == K_DOWN: self.posicao_da_escolha -= 1
                    
                    if event.key == K_z:
                        match self.posicao_da_escolha:
                            case 3: self.running = False
                            case 2: Credits()
                            case 1: self.running = False
                    
            self.logic()
            pygame.display.flip()
            
    
    def logic(self):
        
        # limitar a posição da escolha
        match self.posicao_da_escolha:
            case 0: self.posicao_da_escolha = 3
            case 4: self.posicao_da_escolha = 1
        
        # dar o highlight aos botões (hover)
        for button in self.buttons:
            if button == self.buttons[self.posicao_da_escolha - 1]: button.hover = True
            else: button.hover = False
        
            
main = Main()
main.start()