import pygame
from core.peon import Peon
from core.constantes import DIMENSION_CASILLAS, COLUMNAS, FILAS, BLANCO, NEGRO


class Tablero:

    def __init__(self):

        self.piezas_Blancas = 12
        self.piezas_Negras = 12
        self.reinas_Blancas = 12
        self.reinas_Negras = 12
        self.tablero = []
        self.inizializar()

    def inizializar(self):
        for col in range(COLUMNAS):
            self.tablero.append([])
            for fil in range(FILAS):
                if col % 2 and fil % 2 and (3 > fil or fil > 4):
                    self.tablero[col].append(Peon(col, fil))
                elif (fil + 1) % 2 and (col + 1) % 2 and (3 > fil or fil > 4):
                    self.tablero[col].append(Peon(col, fil))
                else:
                    self.tablero[col].append(0)

    def pintar_damero(self, WIN):
        WIN.fill(NEGRO)
        for col in range(COLUMNAS):
            for fil in range(col % 2, FILAS, 2):
                pygame.draw.rect(WIN, BLANCO, (col * DIMENSION_CASILLAS, fil * DIMENSION_CASILLAS, DIMENSION_CASILLAS, DIMENSION_CASILLAS))
        
    def pintar_piezas(self, WIN):
        for col in range(COLUMNAS):
            for fil in range(FILAS):
                if self.tablero[col][fil] != 0:
                    self.tablero[col][fil].dibujar(WIN)

    def dibujar_tablero(self, WIN):
        self.pintar_damero(WIN)
        self.pintar_piezas(WIN)
        pygame.display.update()

