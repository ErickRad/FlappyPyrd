import pygame

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load("assets/pipe.png"))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load("assets/base.png"))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load("assets/bg.png"))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load("assets/bird1.png")),
    pygame.transform.scale2x(pygame.image.load("assets/bird2.png")),
    pygame.transform.scale2x(pygame.image.load("assets/bird3.png")),
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont(name='roboto', size=30)

ROTACAO_MAXIMA = 0
VELOCIDADE_ROTACAO = 20
TEMPO_ANIMACAO = 5
TELA_LARGURA = 500
TELA_ALTURA = 800
DIFICULDADE = 0