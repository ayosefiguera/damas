import pygame
from core.constantes import WIDTH, HEIGHT, FPS, DIMENSION_CASILLAS
from core.tablero import Tablero
from core.game import Game


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Damas')

def piece_position(event_pos):
    x, y = event_pos
    return int(x // DIMENSION_CASILLAS), int(y // DIMENSION_CASILLAS)


def main():
    juego = Game()
    clock = pygame.time.Clock()
    run = True

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                col, row = piece_position(event.pos)
                juego.select(col, row)
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                juego.restart()

            if event.type == pygame.QUIT:
                run = False
        juego.draw(WIN)    
main()
