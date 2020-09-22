import pygame
from core.setup import WIDTH, HEIGHT, FPS, SQUARE_SIZE
from core.board import Board


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Damas')
board = Board()

def get_row_col_from_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
            if event.type == pygame.MOUSEBUTTONDOWN:
               pos = pygame.mouse.get_pos()
               row, col = get_row_col_from_mouse(pos)
               piece = board.get_piece(row, col)
               board.move(piece, 7, 0)

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()
