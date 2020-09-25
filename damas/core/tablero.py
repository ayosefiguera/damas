import pygame
from damas.core.constantes import DIMENSION_CASILLAS, COLUMNAS, FILAS, BLANCO, NEGRO
from damas.core.peon import Peon


class Tablero:

    def __init__(self,):

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
                if col % 2 and fil % 2:
                    self.tablero[col].append(Peon(col, fil))
                elif col + 1 % 2 and fil + 1 % 2:
                    self.tablero[col].append(Peon(col, fil))
                else:
                    self.tablero[col].append(0)

    def dibujar(self):
        for col in range(COLUMNAS):
            for fil in range(FILAS):
                if col % 2 and fil % 2:
                    #TODO PINTAR color Negro.
                    pass
                elif not col % 2 and not fil % 2:
                    #TODO PINTAR COLOR Negro.
                    pass
                else:
                    #TODO PINTAR COLOR Blanco,
                    pass