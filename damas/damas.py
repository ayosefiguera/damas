import pygame
from core.constantes import WIDTH, HEIGHT, FPS
from core.tablero import Tablero


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Damas')


def main():
    juego = Tablero()
    clock = pygame.time.Clock()
    run = True

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        juego.dibujar_tablero(WIN)
        
main()
