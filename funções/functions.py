import pygame, random
from pygame.locals import *
from globals import *

# ---------------------------------------------------------------------------------------------------------------------------------------------

class button: # Classe que cria um botão onde quiser com posição, tamanho e cor  
    def __init__(self, pos, size, color, text = '', corner_radius = 0, hover_color = (255, 255, 255)):
        
        self.pos = pos
        self.size = size
        self.color = color
        self.text = text
        self.corner_radius = corner_radius
        self.hover_color = hover_color
        self.hover = False
        
        self.rect = pygame.Rect((0, 0), self.size)
        self.rect.center = self.pos
        
    def show(self):
        
        if self.hover:
            pygame.draw.rect(window.display, self.hover_color, self.rect, 0, self.corner_radius)
        else:
            pygame.draw.rect(window.display, self.color, self.rect, 0, self.corner_radius)

# ---------------------------------------------------------------------------------------------------------------------------------------------
        
class write:
    def __init__(self, text, pos, size, color):
        
        self.size = size
        self.text = text
        self.color = color
        self.pos = pos
        self.font = pygame.font.Font(None, self.size)
        self.write = self.font.render(self.text, 0, self.color)
        self.rect = self.write.get_rect()
        self.rect.center = self.pos
        self.update()
        
    def update(self):
        
        window.display.blit(self.write, self.rect)
        
# ---------------------------------------------------------------------------------------------------------------------------------------------


def CalculoDanoFisico(danoFisico, defesaFisica):
    DanoFisicoCausado = danoFisico * (50/(50+defesaFisica)) #DEFESA FISICA DO INIMIGO
    return f"{DanoFisicoCausado:.0f}"


def CalculoDanoMagico(danoMagico, defesaMagica):
    DanoMagicoCausado = danoMagico * (50/(50+defesaMagica)) #DEFESA MAGICA DO INIMIGO
    return f"{DanoMagicoCausado:.0f}"
    
    
# ---------------------------------------------------------------------------------------------------------------------------------------------


def MaiorAgilidade(listadepersonagens):
    agilidades = []
    for personagem in listadepersonagens:
        agilidades.append(personagem.agilidade)
    agilidades.sort(reverse=True)
    for personagem in listadepersonagens:
        for agilidade in agilidades:
            if personagem.agilidade == agilidade:
                agilidades.insert(agilidades.index(agilidade), personagem)
                agilidades.remove(agilidade)
    return agilidades


# ---------------------------------------------------------------------------------------------------------------------------------------------


def SortearInimigos(inimigos):
    lista_de_inimigos = []
    lista_de_inimigos.append(inimigos[random.randint(0, len(inimigos) - 1)])
    lista_de_inimigos.append(inimigos[random.randint(0, len(inimigos) - 1)])
    lista_de_inimigos.append(inimigos[random.randint(0, len(inimigos) - 1)])
    return lista_de_inimigos


# ---------------------------------------------------------------------------------------------------------------------------------------------


class IA:
    
    def __init__(self, turnoatual, personagens):
        
        self.escolha = random.randint(0, 2)
        self.turnoatual = turnoatual
        self.personagens = personagens
        match self.escolha:
            case 0: return self.turnoatual.ataque1(self.personagens[random.randint(0, len(self.personagens) - 1)].nome)
            case 1: return self.turnoatual.ataque2(self.personagens[random.randint(0, len(self.personagens) - 1)].nome)
            case 2: return self.turnoatual.defesa()