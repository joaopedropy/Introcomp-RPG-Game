import pygame
from pygame.locals import *
from globals import *
from funções.functions import write, button
from batalha import Batalha

pygame.init()

class Choose_Menu:              # Classe que será rodada a partir do Main Menu
    def __init__(self):
        
        self.running = True     # Ir ou não ao menu principal
        
        # Outros
        self.choose = 1   # Posição de escolha
        self.fading_to_game = False  # transição em fade
        self.alpha = 255   # componente da transição
        
        # Background
        self.background = pygame.image.load("backgrounds/choose menu background.jpg").convert()   # placeholder por enquanto
        self.background = pygame.transform.scale(self.background, (screen_x, screen_y))           # Transformar a escala do placeholder
        
        # Sistema de escolhas
        self.choices = []   # lista com o nome dos personagens escolhidos
        self.number_of_characters_choosed = 0    # limitador de escolhas
        
        # characters (carregar botões e carregar a imagem)
        # retângulos
        self.mago = button((screen_x // 4, 350), (180, 180), cinza)   # Todos os botões de personagens para facilitar a visualização
        self.ladino = button((screen_x // 2, 350), (180, 180), cinza)
        self.paladino = button((screen_x // 1.35, 350), (180, 180), cinza)
        self.sacerdote = button((screen_x // 2.55, 600), (180, 180), cinza)
        self.cacador = button((screen_x // 1.65, 600), (180, 180), cinza)
        
        # lista de personagens pra facilitar minha vida
        list_of_characters = [self.mago, self.ladino, self.paladino, self.sacerdote, self.cacador]       # Ter um controle do que será selecionado
        list_of_names = ["Mago", "Ladino", "Paladino", "Sacerdote", "Caçador"]       # Ter um controle do que será selecionado
        self.character_pos = 0     # Ter um controle do que será selecionado (puxar depois na lista)
        
        
        # imagens
        self.magoimg = pygame.transform.scale(pygame.image.load("personagens/mago.png").convert_alpha(), self.mago.size)    # Placeholder
        self.ladinoimg = pygame.transform.scale(pygame.image.load("personagens/ladino.png").convert_alpha(), self.ladino.size)    # Placeholder
        self.paladinoimg = pygame.transform.scale(pygame.image.load("personagens/paladino.png").convert_alpha(), self.paladino.size)    # Placeholder
        self.sacerdoteimg = pygame.transform.scale(pygame.image.load("personagens/sacerdote.png").convert_alpha(), self.sacerdote.size)    # Placeholder
        self.cacadorimg = pygame.transform.scale(pygame.image.load("personagens/caçador.png").convert_alpha(), self.cacador.size)    # Placeholder
        
        # loop principal
        while self.running:
            
            # dar update na tela
            screen.fill(preto)
            display.fill((200, 200, 200))
            display.set_alpha(255)
            display.blit((self.background), (0, 0))    # Placeholder
            
            # Título Menu de escolha
            write("Escolha 3 Personagens", (screen_x // 2, screen_y // 5), 70, (branco))
            
            # Debug of choose
            write(f"{self.choose}", (25, 25), 24, (branco))    # apenas para testar se a posição está correta
            
            # desenhar quadrados dos personagens e nomes
            for character in list_of_characters:     # desenhar os quadrados de seleção
                character.update(rounded_edge=10)
                write(f"{list_of_names[list_of_characters.index(character)]}", (character.rect.midtop[0], character.rect.midtop[1] - 20), 34, branco)
            
            # draw Characters
            display.blits(((self.magoimg, self.mago), (self.cacadorimg, self.cacador), (self.sacerdoteimg, self.sacerdote), (self.paladinoimg, self.paladino), (self.ladinoimg, self.ladino)))  # Desenhar as imagens # Placeholder
            
            # quit event
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()
                    
                # Eventos do teclado
                # return to main menu
                if event.type == KEYDOWN:
                    if event.key == K_x:
                        self.running = False
                    
                    # choosing character
                    if event.key == K_z:
                        if self.number_of_characters_choosed == 2:  # Limit on 3 characters
                            self.fading_to_game = True     # Iniciar o jogo
                            
                        if self.number_of_characters_choosed != 3:  # Choosing the 3 characters
                            if list_of_names[self.choose - 1] not in self.choices:
                                self.choices.append(list_of_names[self.choose - 1])
                                self.number_of_characters_choosed += 1
                            else:
                                print("character already in list")   # apenas para debug, logo será implementado como uma mensagem na tela
                        
                    # change the pos of choose
                    if event.key == K_RIGHT:    # alterar a escolha
                        self.choose += 1
                    elif event.key == K_LEFT:    # alterar a escolha 
                        self.choose -= 1
                        
            # Limitar a escolha entre 1 e 5 personagens no menu (não deixar a posição sair de 1 - 5)
            match self.choose:
                case 6: self.choose = 1
                case 0: self.choose = 5
            
            # glow na seleção de personagem  (destacar o quadrado)
            for character in list_of_characters:
                if list_of_characters.index(character) == self.choose - 1:
                    character.color = branco
                else:
                    character.color = cinza
                
            # Transição em fade para a tela de batalha
            if self.fading_to_game:
                self.alpha -= 1
                if self.alpha <= 5:
                    
                    # definir escolhas
                    escolhas.personagem1 = self.choices[0]
                    escolhas.personagem2 = self.choices[1]
                    escolhas.personagem3 = self.choices[2]
                    print(escolhas.personagem1, escolhas.personagem2, escolhas.personagem3)   # apenas para debug
                    
                    Batalha()    # iniciar a batalha
                    self.alpha = 255  # resetar a tela
                    self.fading_to_game = False    # resetar a tela
                    
                display.set_alpha(self.alpha)     # resetar a tela
   
                
            # dar update em tudo            
            screen_update()
            pygame.display.update()

# Teste
Choose_Menu()   # debugger