import pygame
from pygame.locals import *
from globals import *
from funções.functions import button, write
from choose_menu import Choose_Menu
# from impmusicas import *

pygame.init()

# Botões (definir)
start_button = button((screen_x //2, screen_y // 2), (200, 100), (branco))
quit_button = button((screen_x //2, screen_y // 1.5), (200, 100), (branco))

# Outros 
alpha = 255 # fade alpha
fading_to_game = False # fade condition
choose = 1
background = pygame.image.load("backgrounds/main menu background.png").convert()
background = pygame.transform.scale(background, (screen_x, screen_y))

# loop principal
while True:
    
    screen.fill(preto)
    display.fill((150, 150, 150))
    display.set_alpha(255) # NÃO MEXER
    display.blit(background, (0, 0))
    
    # Título principal
    write("Jogo", (screen_x // 2, screen_y // 3), 80, (preto))
    
    # Debug
    write(f"{choose}", (25, 25), 12, (preto))
    
    # Botões ( escrever e desenhar )
    start_button.update(rounded_edge=20), write("Start", start_button.rect.center, 40, (0, 0, 0))
    quit_button.update(rounded_edge=20), write("Quit", quit_button.rect.center, 40, (0, 0, 0))
    
    # Eventos em geral
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        # Teclado
        if event.type == KEYDOWN:
            if event.key == K_UP:
                choose += 1
            elif event.key == K_DOWN:
                choose -= 1
            if event.key == K_z or event.key == K_RETURN:
                match choose:
                    case 1: fading_to_game = True
                    case 2: pygame.quit()
                
    # Controle do player sobre o menu (escolher entre jogar e sair)
    match choose:
        case 1: write(">", (start_button.rect.midleft[0] - 20, start_button.rect.midleft[1]), 80, (0, 0, 0))
        case 2: write(">", (quit_button.rect.midleft[0] - 20, quit_button.rect.midleft[1]), 80, (0, 0, 0))
        case 3: choose = 1
        case 0: choose = 2
                
    # Transição em fade para a tela de escolha
    if fading_to_game:
        alpha -= 2
        if alpha <= 5:
            Choose_Menu()
            alpha = 255
            fading_to_game = False
        display.set_alpha(alpha)
    
    # Atualizar a tela
    screen_update()
    pygame.display.flip()
    
print("Hello world")