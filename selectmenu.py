import pygame
from pygame.locals import *
from globals import *
from funções.functions import Button, write
from musicas.musiccontrol import radio
from game import Game


pygame.init()


class SelectMenu:
    def __init__(self): # todas as minhas variáveis que vão ser usadas na classe
        
        self.running = True # condição da tela
        radio.play("musicas/Seleção.wav") # música da tela
        self.background = pygame.image.load("backgrounds/selectmenubg.png") # background
        
        self.posicao_da_escolha = 1
        
        
        self.mago = Button(   # Botão de start; definições
            pos = (230, window.rect.centery - 100),
            size = (200, 200),
            color = cores.verde_claro,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            hover_size = (220, 220),
            anchor="center",
            text = "Mago",
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        
        self.ladino = Button(   # Botão de start; definições
            pos = (500, window.rect.centery - 100),
            size = (200, 200),
            color = cores.verde_claro,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            hover_size = (220, 220),
            anchor="center",
            text = "Ladino",
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        
        self.paladino = Button(   # Botão de start; definições
            pos = (770, window.rect.centery - 100),
            size = (200, 200),
            color = cores.verde_claro,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            hover_size = (220, 220),
            anchor="center",
            text = "Paladino",
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        
        self.sacerdote = Button(   # Botão de start; definições
            pos = (365, window.rect.centery + 180),
            size = (200, 200),
            color = cores.verde_claro,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            hover_size = (220, 220),
            anchor="center",
            text = "Sacerdote",
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        
        self.cacador = Button(   # Botão de start; definições
            pos = (635, window.rect.centery + 180),
            size = (200, 200),
            color = cores.verde_claro,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            hover_size = (220, 220),
            anchor="center",
            text = "Caçador",
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        
        self.buttons = [
            self.mago,
            self.ladino,
            self.paladino,
            self.sacerdote,
            self.cacador
        ]
        self.selected = []
        
        
        self.start() # inicia o loop principal
        
    def start(self):
        while self.running:
            window.start(bg = self.background)
            self.draw()
            
            
            for event in pygame.event.get():
                if event.type == QUIT: self.exit() # evento de sair
                if event.type == KEYDOWN:
                    if event.key == K_LEFT: self.posicao_da_escolha -= 1
                    elif event.key == K_RIGHT: self.posicao_da_escolha += 1
                    elif event.key == K_z: self.select_character()
                    
                    
            self.logic()
            pygame.display.flip()
            
            
    def select_character(self):
        
        for button in self.buttons:
            if button == self.buttons[self.posicao_da_escolha - 1] and button not in self.selected:
                self.selected.append(button)
            
    def logic(self):
        
        match self.posicao_da_escolha:
            case 6: self.posicao_da_escolha = 1
            case 0: self.posicao_da_escolha = 5
            
        for button in self.buttons:
            if button not in self.selected:
                if button == self.buttons[self.posicao_da_escolha - 1]: button.hover = True
                else: button.hover = False
            else: 
                button.color = cores.azul_claro
                button.hover = False
                
        if len(self.selected) == 3:
            self.confirm_selection()
            
            
    def confirm_selection(self):
        
        self.confirming = True
        
        while self.confirming:
            
            window.start(bg = self.background)
            
            write("Deseja escolher esses 3 personagens?", (window.rect.centerx, window.rect.centery - 200), 55, (230, 230, 230))
            write(self.selected[0].text, (window.rect.centerx - 200, window.rect.centery - 80), 40, cores.azul_claro)
            write(self.selected[1].text, (window.rect.centerx, window.rect.centery - 80), 40, cores.azul_claro)
            write(self.selected[2].text, (window.rect.centerx + 200, window.rect.centery - 80), 40, cores.azul_claro)
            write("Sim (pressione Z)", (window.rect.centerx // 2, window.rect.centery + 50), 45, (230, 230, 230))
            write("Não (pressione X)", (window.rect.centerx + window.rect.centerx // 2, window.rect.centery +50), 45, (230, 230, 230))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.confirming = False
                    self.running = False
                    
                    
                if event.type == KEYDOWN:
                    if event.key == K_z: 
                        escolhas.escolha1 = self.selected[0]
                        escolhas.escolha2 = self.selected[1]
                        escolhas.escolha3 = self.selected[2]
                        self.confirming = False
                        self.running = False
                        Game()
                    elif event.key == K_x: 
                        self.confirming = False
                        self.running = False
            
            pygame.display.update()
    
            
    def draw(self):
        
        write("Escolha 3 personagens", (window.rect.centerx, window.rect.centery - 300), 55, (255, 255, 255))
        
        for button in self.buttons:
            button.show()
            
            
    def exit(self):
        
        radio.play("musicas/Menu.wav")
        self.running = False
        

# SelectMenu()