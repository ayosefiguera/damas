import pygame
from .peon import Peon
from .constantes import DIMENSION_CASILLAS, COLUMNAS, FILAS, BLANCO, NEGRO, AMARILLO


class Tablero:

    def __init__(self):

        self.piezas_Blancas = 12
        self.piezas_Negras = 12
        self.reinas_Blancas = 12
        self.reinas_Negras = 12
        self.tablero = []
        self.initiate()
        self.validate = []

    def initiate(self):
        for col in range(COLUMNAS):
            self.tablero.append([])
            for fil in range(FILAS):
                if col % 2 and fil % 2 and (3 > fil or fil > 4):
                    self.tablero[col].append(Peon(col, fil))
                elif (fil + 1) % 2 and (col + 1) % 2 and (3 > fil or fil > 4):
                    self.tablero[col].append(Peon(col, fil))
                else:
                    self.tablero[col].append(0)

    def draw_damero(self, WIN):
        WIN.fill(NEGRO)
        for col in range(COLUMNAS):
            for fil in range(col % 2, FILAS, 2):
                pygame.draw.rect(WIN, BLANCO, (col * DIMENSION_CASILLAS, fil * DIMENSION_CASILLAS, DIMENSION_CASILLAS, DIMENSION_CASILLAS))
        
    def draw_piezas(self, WIN):
        for col in range(COLUMNAS):
            for fil in range(FILAS):
                if self.tablero[col][fil] != 0:
                    self.tablero[col][fil].draw(WIN)

    def draw_validate(self, WIN):
        print('dibujando validaciones')
        for pos in self.validate:
            print(f'{pos}')
            x = pos[0] * DIMENSION_CASILLAS + DIMENSION_CASILLAS//2
            y = pos[1] * DIMENSION_CASILLAS + DIMENSION_CASILLAS//2
            pygame.draw.circle(WIN,(0,255,0),(x,y), 15)

    def get_from_pos(self, col, fila):
        return self.tablero[col][fila]

    def mov(self, pieza, col, fila):
        self.tablero[pieza.columna][pieza.fila] = 0
        pieza.mov(col, fila)
        pieza.swicht_Select()
        self.tablero[col][fila] = pieza

    def restart_validate(self):
        self.validate = []
    
    
    def get_valid_mov(self, piece):
        self.restart_validate()
        self.scan_left(piece.columna, piece.fila, piece.color)
        self.scan_right(piece.columna, piece.fila, piece.color)

    def is_Validate(self, pos):
        if pos in self.validate:
            return True
        else:
            return False

    def scan(self, pos):

        if 0 <= abs(pos[0]) <= 7 and 0 <= abs(pos[1]) <= 7:
            casilla = self.get_from_pos(pos[0], pos[1]) 
            return pos, casilla
        else:
            return pos, False
        
    def scan_left(self, row, col, color, skip=False):

        if color == BLANCO:
            pos, casilla = self.scan((row - 1, col + 1))

        else:
            pos, casilla = self.scan((row - 1, col - 1))

        if casilla != 0 and casilla != color and skip == False:

            self.scan_left(pos[0], pos[1], color, skip=True)

        elif casilla == 0:
            self.validate.append(pos)

    def scan_right(self,  row, col, color, skip=False):

        if color == BLANCO:
            pos, casilla = self.scan((row + 1, col + 1))
        else:
            pos, casilla = self.scan((row + 1, col - 1))
        
        if casilla != 0 and casilla != color and skip == False:
            
            self.scan_right(pos[0], pos[1], color, skip=True)

        elif casilla == 0:
            self.validate.append(pos)
        


    def draw(self, WIN):
        self.draw_damero(WIN)
        self.draw_piezas(WIN)
        self.draw_validate(WIN)
        pygame.display.update()

    def select_piece(self, piece):
        piece.swicht_Select()


