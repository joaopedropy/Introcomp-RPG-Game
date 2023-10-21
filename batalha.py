import pygame
from pygame.locals import *
from globals import *
from funções.functions import MaiorAgilidade, SortearInimigos, IA
from personagens.aliados import JMago, JPaladino, JLadino, JCaçador, JSacerdote
from personagens.inimigos import *
from impmusicas import *
from batalha_assets.menu_de_ataque import MenuDeEscolha, MenuDeAtaque

pygame.init()

class Batalha:
    def __init__(self):
        
        self.running = True    # iniciar o jogo e permitir que retorne para a tela principal
        
        # Background
        self.background = pygame.image.load("backgrounds/batalha background.png").convert()  # Placeholder
        self.background = pygame.transform.scale(self.background, (screen_x, screen_y))   # Placeholder transformar
        

        # Escolha de personagens ( colocar na classe )
        list_of_characters = [JMago, JLadino, JPaladino, JSacerdote, JCaçador]    # para a escolha de personagens ( a classe de cada )
        list_of_enemies = [Inimigo1, Inimigo2, Inimigo3, Inimigo4, Inimigo5]
        list_of_names = ["Mago", "Ladino", "Paladino", "Sacerdote", "Caçador"]    # para pegar a escolha que já foi passada
        escolhas.personagem1 = list_of_characters[list_of_names.index(escolhas.personagem1)]
        escolhas.personagem2 = list_of_characters[list_of_names.index(escolhas.personagem2)]
        escolhas.personagem3 = list_of_characters[list_of_names.index(escolhas.personagem3)]
        
        
        # Sortear os inimigos e classificar de acordo com a agilidade player e inimigo
        self.enemies = SortearInimigos(list_of_enemies)  # Sortear inimigos
        self.personagens = [escolhas.personagem1, escolhas.personagem2, escolhas.personagem3]  # minha lista de personagens
        self.maioragilidadeplayer = MaiorAgilidade(self.personagens)
        self.maioragilidadeinimigo = MaiorAgilidade(self.enemies) 
        

        # turnos
        self.personagem = 0
        self.turno_ativo = True
        self.turno_player = self.maioragilidadeplayer
        self.turno_inimigos = self.maioragilidadeinimigo
        self.turno_atual = self.turno_player[self.personagem]
        
        
        # Outros
        self.alpha = 0    # fade inicial
        self.fading_to_game = True    # fade inicial
        self.fading_to_end = False    # fade inicial
        
        
        # Escolhas do menu
        self.click = False
        self.escolhadeacao = 1
        self.estado = "escolhendo ataque"
        self.comando = None
        self.escolheu = False
        
        
        # loop principal
        while self.running:
            # musicaBatalha()
            
            # atualizar a tela
            screen.fill(preto)
            display.fill((branco))
            display.blit(self.background, (0, 0))   # Placeholder
            
            
            # Eventos
            # Sair
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    
                # Teclas direita e esquerda
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.escolhadeacao += 1
                    if event.key == K_LEFT:
                        self.escolhadeacao -= 1
                        
                    # Tecla selecionar ou não o ataque/defesa
                    if event.key == K_z:
                        self.click = True
                    
            # Transição em fade para a tela de batalha
            if self.fading_to_game:
                self.alpha += 1
                if self.alpha >= 255:
                    self.fading_to_game = False
                display.set_alpha(self.alpha)
                
            if self.turno_ativo:
                # botões (limit)
                match self.escolhadeacao:
                    case 4: self.escolhadeacao = 1
                    case 0: self.escolhadeacao = 3
                    
                # Menu de escolha de ataque
                
                self.menudeescolha = MenuDeEscolha(self.turno_atual)
                self.menudeataque = MenuDeAtaque(self.enemies)
                    
                if self.estado == "escolhendo ataque":
                    for botao in self.menudeescolha.botoes:
                        if self.menudeescolha.botoes.index(botao) == self.escolhadeacao - 1:
                            botao.color = (200, 200, 200)
                            if self.click:
                                if botao.nome != "defesa":
                                    self.estado = "escolhendo inimigo"
                                    self.comando = botao.nome
                                    self.click = False
                                else:
                                    self.comando = "defesa"
                        else:
                            botao.color = branco
                    self.menudeescolha.update()  
                            
                if self.estado == "escolhendo inimigo":
                    for botao in self.menudeataque.botoes:
                        if self.menudeataque.botoes.index(botao) == self.escolhadeacao - 1:
                            botao.color = (200, 200, 200)
                            if self.click:
                                self.menudeataque.escolha = botao.nome
                                self.click = False
                                self.escolheu = True
                                for enemy in self.enemies:
                                    if enemy.nome == self.menudeataque.escolha:
                                        self.menudeataque.escolha = enemy
                                        print(self.menudeataque.escolha)
                        else:
                            botao.color = branco
                    self.menudeataque.update()
                    
                if self.escolheu:
                    if self.comando == "ataque1":
                        self.turno_atual.ataque1(self.menudeataque.escolha)
                        self.escolheu = False
                    if self.comando == "ataque2":
                        self.turno_atual.ataque2(self.menudeataque.escolha)
                        self.escolheu = False
                    if self.comando == "defesa":
                        self.turno_atual.defesa()
                        self.escolheu = False
                    if self.personagem < 2:
                        self.personagem += 1
                    else:
                        self.turno_ativo = False
                        self.personagem = 0
                    self.turno_atual = self.turno_player[self.personagem]
                    self.estado = "escolhendo ataque"
                
            else:
                self.turno_atual = self.turno_inimigos[self.personagem]
                print(IA(self.turno_atual, self.personagens))
                print("\n\n\n")
                pygame.quit()
                
            
            # Atualizar tudo
            screen_update()
            pygame.display.update()