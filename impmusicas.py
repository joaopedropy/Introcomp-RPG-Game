import pygame

def musicaSeleção():
    # Inicialize o Pygame
    pygame.init()

    # Inicialize o mixer de áudio
    pygame.mixer.init()

    # Carregue a música
    pygame.mixer.music.load('musicas/boiSeleção.wav')

    # Defina o evento de término da música
    MUSIC_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(MUSIC_END)

    # Comece a reproduzir a música
    pygame.mixer.music.play()

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MUSIC_END:
                # A música terminou, reproduza-a novamente
                pygame.mixer.music.play()

    # Encerre o Pygame
    pygame.quit()


def musicaBatalha():
    # Inicialize o Pygame
    pygame.init()

    # Inicialize o mixer de áudio
    pygame.mixer.init()

    # Carregue a música
    pygame.mixer.music.load('musicas/dyingBatalha.wav')

    # Defina o evento de término da música
    MUSIC_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(MUSIC_END)

    # Comece a reproduzir a música
    pygame.mixer.music.play()

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MUSIC_END:
                # A música terminou, reproduza-a novamente
                pygame.mixer.music.play()

    # Encerre o Pygame
    pygame.quit()


def musicaMenu():
    # Inicialize o Pygame
    pygame.init()

    # Inicialize o mixer de áudio
    pygame.mixer.init()

    # Carregue a música
    pygame.mixer.music.load('bounceMenu.wav')

    # Defina o evento de término da música
    MUSIC_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(MUSIC_END)

    # Comece a reproduzir a música
    pygame.mixer.music.play()

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MUSIC_END:
                # A música terminou, reproduza-a novamente
                pygame.mixer.music.play()

    # Encerre o Pygame
    pygame.quit()