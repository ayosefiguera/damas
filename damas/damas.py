import pygame
from core.constantes import WIDTH, HEIGHT



WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Damas')


def main():
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()