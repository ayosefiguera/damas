import pygame
from .constantes import NEGRO, BLANCO, DIMENSION_CASILLAS, GRIS, BLANCO, NEGRO, CORONA, AMARILLO

class Peon:
    RADIUS = 25
    PADDING = 3

    def __init__(self, columna, fila):
        
        self.columna = columna
        self.fila = fila
        self.reina = False
        self.color = self.color_init()
        self.select = False

    def soy_reina(self):
        self.reina = True

    def swicht_Select(self):
        if self.select:
            self.select = False
        else:
            self.select = True

    def mov(self, columna, fila):
        self.fila = fila
        self.columna = columna
        if fila == 0 or fila == 7:
           self.soy_reina()

    def color_init(self):
        if self.fila < 4:
            return BLANCO
        else:
            return NEGRO
            
    def calc_position(self):
        x = self.columna * DIMENSION_CASILLAS + DIMENSION_CASILLAS // 2
        y = self.fila*DIMENSION_CASILLAS + DIMENSION_CASILLAS//2
        return x, y

    def draw(self, WIN):
        x, y = self.calc_position()

        if self.select:
            pygame.draw.circle(WIN, AMARILLO, (x, y), self.RADIUS + self.PADDING)
        else:
            pygame.draw.circle(WIN, GRIS, (x, y), self.RADIUS + self.PADDING)

        pygame.draw.circle(WIN, self.color, (x, y), self.RADIUS)

        if self.reina:
            WIN.blit(CORONA, (x - CORONA.get_width() //
                              2, y - CORONA.get_height()//2))

    def __repr__(self):
        return self.color

    def __str__(self):
        return f'Peon{self.color}'
