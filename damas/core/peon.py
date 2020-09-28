import pygame
from .constantes import NEGRO, BLANCO, DIMENSION_CASILLAS, GRIS, BLANCO, NEGRO, CORONA

class Peon:
    RADIUS = 25
    PADDING = 3

    def __init__(self, columna, fila):
        
        self.columna = columna
        self.fila = fila
        self.reina = False
        self.color = self.color_init()

    def soy_reina(self):
        self.reina = True

    def mover(self, columna, fila):
        self.fila = fila
        self.columna = columna

    def color_init(self):
        if self.fila < 4:
            return BLANCO
        else:
            return NEGRO
            
    def calcular_posicion(self):
        return self.columna*DIMENSION_CASILLAS + DIMENSION_CASILLAS//2, self.fila*DIMENSION_CASILLAS + DIMENSION_CASILLAS//2

    def dibujar(self, WIN):
        x, y = self.calcular_posicion()

        pygame.draw.circle(WIN, GRIS, (x, y), self.RADIUS + self.PADDING)
        pygame.draw.circle(WIN, self.color, (x, y), self.RADIUS)

        if self.reina:
            WIN.blit(CORONA, (x - CORONA.get_width() //
                              2, y - CORONA.get_height()//2))

    def __repr__(self):
        return self.color

    def __str__(self):
        return f'Peon {self.color} POS{self.columna},{self.fila}'
