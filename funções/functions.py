import pygame, random
from pygame.locals import *
from globals import *

# ---------------------------------------------------------------------------------------------------------------------------------------------

class Button: # Classe que cria um botão onde quiser com posição, tamanho e cor  
    def __init__(self, pos, size, color, text = '', text_size = 30, text_color = (255, 255, 255), text_hover_color = (0, 0, 0), corner_radius = 0, hover_color = (255, 255, 255), border_width = 0, border_color = (0, 0, 0), anchor = "center", hover_size = (350, 70)):
        
        self.pos = pos
        self.size = size
        self.color = color
        self.text = text
        self.text_size = text_size
        self.text_color = text_color
        self.text_hover_color = text_hover_color
        self.corner_radius = corner_radius
        self.hover_color = hover_color
        self.hover = False
        self.border_width = border_width
        self.border_color = border_color
        self.anchor = anchor
        self.hover_size = hover_size
        
        self.rect = pygame.Rect((0, 0), self.size)
        
        if anchor == "center": self.rect.center = self.pos
        elif anchor == "left": self.rect.topleft = self.pos
        elif anchor == "right": self.rect.topright = self.pos
            
        
    def show(self):
        
        if self.hover:
            self.rect.size = self.hover_size
            pygame.draw.rect(window.display, self.hover_color, self.rect, 0, self.corner_radius)
            write(self.text, self.rect.center, int(f"{self.text_size * 1.2:.0f}"), self.text_hover_color)
        else:
            self.rect.size = self.size
            pygame.draw.rect(window.display, self.color, self.rect, 0, self.corner_radius)
            write(self.text, self.rect.center, self.text_size, self.text_color)
        
        if self.border_width > 0:
            pygame.draw.rect(window.display, self.border_color, self.rect, self.border_width, self.corner_radius)

# ---------------------------------------------------------------------------------------------------------------------------------------------
        
class write:
    def __init__(self, text, pos, size, color):
        
        self.size = size
        self.text = text
        self.color = color
        self.pos = pos
        self.font = pygame.font.Font(None, self.size)
        self.write = self.font.render(self.text, True, self.color)
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