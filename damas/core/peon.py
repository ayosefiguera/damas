import pygame
from .constantes import NEGRO, BLANCO, DIMENSION_CASILLAS, GRIS, BLANCO, NEGRO, CORONA, AMARILLO

class Peon:
    RADIUS = 25
    PADDING = 3

    def __init__(self, col, row):
        
        self.col = col
        self.row = row
        self.queen = False
        self.color = self.color_init()
        self.select = False

    def soy_queen(self):
        self.queen = True

    def swicht_Select(self):
        if self.select:
            self.select = False
        else:
            self.select = True

    def mov(self, col, row):
        self.row = row
        self.col = col
        if row == 0 or row == 7:
           self.soy_queen()

    def color_init(self):
        if self.row < 4:
            return BLANCO
        else:
            return NEGRO
            
    def calc_position(self):
        x = self.col * DIMENSION_CASILLAS + DIMENSION_CASILLAS // 2
        y = self.row*DIMENSION_CASILLAS + DIMENSION_CASILLAS//2
        return x, y

    def draw(self, WIN):
        x, y = self.calc_position()

        if self.select:
            pygame.draw.circle(WIN, AMARILLO, (x, y), self.RADIUS + self.PADDING)
        else:
            pygame.draw.circle(WIN, GRIS, (x, y), self.RADIUS + self.PADDING)

        pygame.draw.circle(WIN, self.color, (x, y), self.RADIUS)

        if self.queen:
            WIN.blit(CORONA, (x - CORONA.get_width() //
                              2, y - CORONA.get_height()//2))

    def __repr__(self):
        return self.color

    def __str__(self):
        return f'Peon{self.color}'
