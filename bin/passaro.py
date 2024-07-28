import pygame
from properties import IMAGENS_PASSARO, ROTACAO_MAXIMA, TEMPO_ANIMACAO, VELOCIDADE_ROTACAO

class Passaro: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = IMAGENS_PASSARO[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < ROTACAO_MAXIMA:
                self.angulo = ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        self.contagem_imagem += 1

        if self.contagem_imagem < TEMPO_ANIMACAO:
            self.imagem = IMAGENS_PASSARO[0]
        elif self.contagem_imagem < TEMPO_ANIMACAO*2:
            self.imagem = IMAGENS_PASSARO[1]
        elif self.contagem_imagem < TEMPO_ANIMACAO*3:
            self.imagem = IMAGENS_PASSARO[2]
        elif self.contagem_imagem < TEMPO_ANIMACAO*4:
            self.imagem = IMAGENS_PASSARO[1]
        elif self.contagem_imagem >= TEMPO_ANIMACAO*4 + 1:
            self.imagem = IMAGENS_PASSARO[0]
            self.contagem_imagem = 0


        if self.angulo <= -80:
            self.imagem = IMAGENS_PASSARO[1]
            self.contagem_imagem = TEMPO_ANIMACAO*2

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)