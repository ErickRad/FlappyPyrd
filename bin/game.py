import pygame
import time
from passaro import Passaro
from cano import Cano
from chao import Chao
from properties import FONTE_PONTOS, IMAGEM_BACKGROUND, TELA_ALTURA, TELA_LARGURA   

def main():
    pygame.display.set_caption(title="FlappyBird")
    pygame.display.set_icon(pygame.image.load("bin/assets/bird2.png"))

    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()

    while True:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                break
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    for passaro in passaros:
                        passaro.pular()

        for passaro in passaros:
            passaro.mover()
        chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)
                    exit()
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True

            cano.mover()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))
        for cano in remover_canos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                passaros.pop(i)

        try:
            tela.blit(IMAGEM_BACKGROUND, (0, 0))
        except pygame.error:
            continue

        
        for passaro in passaros:
            passaro.desenhar(tela)
        for cano in canos:
            cano.desenhar(tela)

        texto = FONTE_PONTOS.render(f"Score: {pontos}", 1, (255, 255, 255))
        tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
        chao.desenhar(tela)
        pygame.display.update()

if __name__ == '__main__':
    time.sleep(1)
    main()
