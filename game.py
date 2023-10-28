import pygame, random
from pygame.locals import *
from globals import window, cores, escolhas
from funções.functions import write, Button
from musicas.musiccontrol import radio
from personagens.aliados import JMago, JLadino, JPaladino, JCaçador, JSacerdote
from personagens.inimigos import Inimigo1, Inimigo2, Inimigo3, Inimigo4, Inimigo5


pygame.init()


class Game:
    def __init__(self):
        
        self.running = True
        radio.play("musicas/Batalha.wav")
        self.background = pygame.image.load("backgrounds/batalha.png") 
        
        # Variáveis das minhas funções
        self.aliados = []  # é usado em definir aliados, definir turno e outros
        self.inimigos = []  # é usado em definir inimigos, definir turno e outros
        self.ordem_de_agilidade = []  # é usado para a função de ordenar por agilidade
        self.personagem_que_esta_atacando = 0   # é utilizado para descobrir qual personagem na lista de personagens (por agilidade) está atacando
        self.turno = 0  # se o turno é player ou inimigo
        self.escolha = 1    # escolha de ataque
        self.ataque_utilizado = None    # ataque utilizado pelo player
        self.inimigo_escolhido = None    # Inimigo escolhido pelo player
        
        # Iniciar minhas funções
        self.definir_aliados()
        self.definir_inimigos()
        self.ordenar_por_agilidade()
        self.identificar_o_turno()
        
        # iniciar a batalha propriamente dita
        self.start()
        
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
        
    def start(self):
        while self.running:
            window.start(bg = self.background)
            
            write(f"{self.ataque_utilizado}", (window.rect.centerx, 45), 40, cores.vinho)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RIGHT: self.escolha += 1  # altera a escolha de ação
                    if event.key == K_LEFT: self.escolha -= 1  # altera a escolha de ação
                    if event.key == K_z and self.turno == "player atacando": self.selecionar_acao()  # Seleciona a ação
                    if event.key == K_z and self.turno == "escolhendo inimigos": self.selecionar_inimigo()  # Seleciona o inimigo
                    if event.key == K_ESCAPE: self.exit()   # sai da batalha --------------------------------------------------------------------- tirar depois
                    
            if self.turno == "player atacando":  # caso seja o turno do player
                self.player_ataca()
            if self.turno == "escolhendo inimigos":
                self.player_escolhe_inimigo()
            
            
            pygame.display.update()
            
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
            
    def player_ataca(self):  # função de identificar e remanejar o ataque do player
        
        self.personagem = self.ordem_de_agilidade[self.personagem_que_esta_atacando]
        self.ataque_menu()
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------    
        
    def ataque_menu(self):   # função que apresenta opções do player
         
        self.ataque_frame = pygame.draw.rect(window.display, (cores.verde_claro), (30, window.rect.centery + 110, 720, 244), 0, 20)
        self.informacoes_frame = pygame.draw.rect(window.display, (cores.verde_claro), (760, window.rect.centery + 110, 234, 244), 0, 20)
        write(f"{self.aliados[0].nome} {self.aliados[0].vida}", (self.informacoes_frame.centerx, self.informacoes_frame.y + 30), 40, cores.vinho)
        write(f"{self.aliados[1].nome} {self.aliados[1].vida}", (self.informacoes_frame.centerx, self.informacoes_frame.y + 90), 40, cores.vinho)
        write(f"{self.aliados[2].nome} {self.aliados[2].vida}", (self.informacoes_frame.centerx, self.informacoes_frame.y + 150), 40, cores.vinho)
        
        self.ataque1 = Button(   # Botão de start; definições
            pos = (self.ataque_frame.x + 10, self.ataque_frame.y + 10),
            size = (300, 100),
            color = cores.vinho,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            hover_size = (305, 105),
            anchor="left",
            text = "Ataque",
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        self.ataque2 = Button(   # Botão de start; definições
            pos = (self.ataque_frame.centerx + 50, self.ataque_frame.y + 10),
            size = (300, 100),
            color = cores.vinho,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            hover_size = (305, 105),
            anchor="left",
            text = self.ordem_de_agilidade[self.personagem_que_esta_atacando].ataqueEspecial,
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        self.defesa = Button(   # Botão de start; definições
            pos = (self.ataque_frame.x + 10, self.ataque_frame.y + 120),
            size = (300, 100),
            color = cores.vinho,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            hover_size = (305, 105),
            anchor="left",
            text = "Defesa",
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        
        self.acoes = [
            self.ataque1,
            self.ataque2,
            self.defesa
        ]
        
        match self.escolha:
            case 4: self.escolha = 1
            case 0: self.escolha = 3
            
        for button in self.acoes:
            if button == self.acoes[self.escolha - 1]:
                button.hover = True
            else:
                button.hover = False
        
        for button in self.acoes:
            button.show()
            
    #-----------------------------------------------------------------------------------------------------------------------------------------------------

    def selecionar_acao(self):
        for acao in self.acoes:
            if acao == self.acoes[self.escolha - 1] and acao != self.defesa:
                self.ataque_utilizado = acao.text
                self.escolha = 1
                self.turno = "escolhendo inimigos"
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    
    def player_escolhe_inimigo(self):
        self.escolher_inimigo_para_atacar()
        
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    
    def escolher_inimigo_para_atacar(self):
        
        self.ataque_frame = pygame.draw.rect(window.display, (cores.verde_claro), (30, window.rect.centery + 110, 720, 244), 0, 20)
        self.informacoes_frame = pygame.draw.rect(window.display, (cores.verde_claro), (760, window.rect.centery + 110, 234, 244), 0, 20)
        write(f"{self.aliados[0].nome} {self.aliados[0].vida}", (self.informacoes_frame.centerx, self.informacoes_frame.y + 30), 40, cores.vinho)
        write(f"{self.aliados[1].nome} {self.aliados[1].vida}", (self.informacoes_frame.centerx, self.informacoes_frame.y + 90), 40, cores.vinho)
        write(f"{self.aliados[2].nome} {self.aliados[2].vida}", (self.informacoes_frame.centerx, self.informacoes_frame.y + 150), 40, cores.vinho)
                
        self.inimigo1 = Button(   # Botão de start; definições
            pos = (self.ataque_frame.x + 10, self.ataque_frame.y + 10),
            size = (300, 100),
            color = cores.vinho,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            hover_size = (305, 105),
            anchor="left",
            text = self.inimigos[0].nome,
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        self.inimigo2 = Button(   # Botão de start; definições
            pos = (self.ataque_frame.centerx + 50, self.ataque_frame.y + 10),
            size = (300, 100),
            color = cores.vinho,
            corner_radius = 20,
            hover_color = cores.azul_esverdeado,
            hover_size = (305, 105),
            anchor="left",
            text = self.inimigos[1].nome,
            text_color = cores.azul_escuro,
            text_hover_color = cores.verde_claro
        )
        
        self.inimigos_para_escolher = [
            self.inimigo1,
            self.inimigo2
        ]
        
        match self.escolha:
            case 3: self.escolha = 1
            case 0: self.escolha = 2
            
        for button in self.inimigos_para_escolher:
            if button == self.inimigos_para_escolher[self.escolha - 1]:
                button.hover = True
            else:
                button.hover = False
        
        for button in self.inimigos_para_escolher:
            button.show()
            
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    
    def selecionar_inimigo(self):
        
        print(self.inimigo1)

        self.atacar()
        
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    
    def atacar(self):
        if self.ataque_utilizado == "Ataque": self.ataque_utilizado = self.personagem.ataque1(self.inimigo_escolhido)
        if self.ataque_utilizado == self.personagem.ataqueEspecial(self.inimigo_escolhido): self.ataque_utilizado = self.personagem.ataque2(self.inimigo_escolhido)
                
    #-----------------------------------------------------------------------------------------------------------------------------------------------------        
            
    def identificar_o_turno(self):
        self.personagem_atacando = self.ordem_de_agilidade[self.personagem_que_esta_atacando]
        if self.personagem_atacando in self.aliados: self.turno = "player atacando"
        elif self.personagem_atacando in self.inimigos: self.turno = "inimigo atacando"
        
        self.personagem_que_esta_atacando += 1
        
        print(self.turno)
        
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
            
    def definir_aliados(self):
        
        self.opcoes = [
            JMago,
            JLadino,
            JPaladino,
            JSacerdote,
            JCaçador
        ]
        
        self.escolhas = [
            escolhas.escolha1,
            escolhas.escolha2,
            escolhas.escolha3
        ]
        
        for escolha in self.escolhas:
            match escolha.text:
                case "Mago": self.aliados.append(JMago)
                case "Ladino": self.aliados.append(JLadino)
                case "Paladino": self.aliados.append(JPaladino)
                case "Sacerdote": self.aliados.append(JSacerdote)
                case "Caçador": self.aliados.append(JCaçador)
                
        for personagem in self.aliados:
            print(f"Escolha: {personagem.nome}")
            
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
            
    def definir_inimigos(self):
        
        self.opcoes = [
            Inimigo1,
            Inimigo2,
            Inimigo3,
            Inimigo4,
            Inimigo5
        ]
        
        for enemy in range(2):
            self.inimigos.append(self.opcoes[random.randint(0, 4)])
            
        for inimigo in self.inimigos:
            print(f"Inimigo: {inimigo.nome}")
            
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
            
    def ordenar_por_agilidade(self):
        
        self.todos_os_personagens = []
        self.todas_as_agilidades = []
        
        for personagem in self.aliados:
            self.todos_os_personagens.append(personagem)
            self.todas_as_agilidades.append(personagem.agilidade)
        for personagem in self.inimigos:
            self.todos_os_personagens.append(personagem)
            self.todas_as_agilidades.append(personagem.agilidade)
            
        self.todas_as_agilidades.sort(reverse=True)
        for personagem in self.todos_os_personagens:
            for agilidade in self.todas_as_agilidades:
                if personagem.agilidade == agilidade:
                    self.todas_as_agilidades[self.todas_as_agilidades.index(agilidade)] = personagem
                    
        self.ordem_de_agilidade = self.todas_as_agilidades
        self.posição = 1
        
        print("Lista por agilidade\n")
        for personagem in self.ordem_de_agilidade:
            print(f"{self.posição}º: {personagem.nome}")
            self.posição += 1
            
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
            
    def exit(self):
        radio.play("musicas/menu.wav")
        self.running = False