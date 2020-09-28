import pygame
#Constantes

WIDTH = HEIGHT = 800
FPS = 60


#Colores
BLANCO = (255, 255 , 240)
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)

CORONA = pygame.image.load('damas/assets/queen.png')

#Tablero
COLUMNAS = FILAS = 8

DIMENSION_CASILLAS = WIDTH / COLUMNAS


