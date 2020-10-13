import pygame
#Constantes

WIDTH = HEIGHT = 800
FPS = 60


#Colores
BLANCO = (255, 255 , 240)
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)
AMARILLO = (204, 255, 229)


#Tablero
COLS = ROWS = 8

DIMENSION_CASILLAS = WIDTH / COLS


#assets
CORONA = pygame.image.load('damas/assets/queen.png')
OPENING = pygame.image.load('damas/assets/Opening.png')
BLACK_TURN = pygame.image.load('damas/assets/Player_black.png')
WHITE_TURN = pygame.image.load('damas/assets/Player_white.png')
WHITE_WIN = pygame.image.load('damas/assets/white_win.png')
BLACK_WIN = pygame.image.load('damas/assets/black_win.png')

