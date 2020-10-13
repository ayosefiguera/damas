import pygame
from .peon import Peon
from .constantes import DIMENSION_CASILLAS, COLS, ROWS, BLANCO, NEGRO, AMARILLO, WHITE_WIN, BLACK_WIN


class Tablero:

    def __init__(self):

        self.pieces_Blancas = 12
        self.pieces_Negras = 12
        self.queens_Blancas = 0
        self.queens_Negras = 0
        self.tablero = []
        self.initiate()
        self.validate = {}

    def initiate(self):
        for col in range(COLS):
            self.tablero.append([])
            for fil in range(ROWS):
                if col % 2 and fil % 2 and (3 > fil or fil > 4):
                    self.tablero[col].append(Peon(col, fil))
                elif (fil + 1) % 2 and (col + 1) % 2 and (3 > fil or fil > 4):
                    self.tablero[col].append(Peon(col, fil))
                else:
                    self.tablero[col].append(0)

    def draw_damero(self, WIN):
        WIN.fill(NEGRO)
        for col in range(COLS):
            for fil in range(col % 2, ROWS, 2):
                pygame.draw.rect(WIN, BLANCO, (col * DIMENSION_CASILLAS, fil * DIMENSION_CASILLAS, DIMENSION_CASILLAS, DIMENSION_CASILLAS))
        
    def draw_pieces(self, WIN):
        for col in range(COLS):
            for fil in range(ROWS):
                if self.tablero[col][fil] != 0:
                    self.tablero[col][fil].draw(WIN)


    def draw_validate(self, WIN):
        for pos in self.validate.keys():
            x = pos[0] * DIMENSION_CASILLAS + DIMENSION_CASILLAS//2
            y = pos[1] * DIMENSION_CASILLAS + DIMENSION_CASILLAS//2
            pygame.draw.circle(WIN,(0,255,0),(x,y), 15)

    def get_from_pos(self, col, row):
        if 0 <= col <= 7 and 0 <= row <= 7:
           return self.tablero[col][row]
        else:
            return 0

    def winner(self):
        if self.pieces_Blancas == 0:
            return BLACK_WIN
        elif self.pieces_Negras == 0:
            return WHITE_WIN
        else:
            return False

    def remove_piece(self, piece):

        self.tablero[piece.col][piece.row] = 0

        if piece.color == BLANCO:
            self.pieces_Blancas -= 1
        else:
            self.pieces_Negras -= 1
        del(piece)

    def mov(self, piece, col, row):

        self.tablero[piece.col][piece.row] = 0
        piece.mov(col, row)
        piece.swicht_Select()
        self.tablero[col][row] = piece
        if self.validate[(col, row)][0] != None:
            for elm in self.validate[(col, row)]:
                self.remove_piece(elm)

    def restart_validate(self):

        self.validate = {}
    
    def get_valid_mov(self, piece, skip=None):
        
        VECTOR_SCAN = [-1, 1]

        if not skip:
            self.restart_validate()

        if piece.color == BLANCO or piece.queen:
            vy = 1
            for vx in VECTOR_SCAN:
                self.scan(piece, vx, vy, skip)

        if piece.color == NEGRO or piece.queen:
            vy = - 1
            for vx in VECTOR_SCAN:
                self.scan(piece, vx, vy, skip)

    def is_Validate(self, pos):

        if pos in self.validate.keys():
            return True
        else:
            return False
  
    def scan(self, piece, vx, vy, skip=None):

            casilla = self.get_from_pos(piece.col + vx, piece.row + vy)

            if casilla != 0 and casilla.color != piece.color and skip == None:
                         
                self.scan(piece, vx+vx, vy+vy, skip=casilla)

            elif skip != None and casilla == 0:
                
                if (piece.col + vx, piece.row + vy) not in self.validate.keys():
                    self.validate[(piece.col + vx, piece.row + vy)] = []

                self.validate[(piece.col + vx, piece.row+ vy)].append(skip)

            elif casilla == 0:
                if (piece.col + vx, piece.row + vy) not in self.validate.keys():
                    self.validate[(piece.col +vx, piece.row + vy)] = []

                self.validate[(piece.col + vx, piece.row + vy)].append(None)


    def draw(self, WIN):
        self.draw_damero(WIN)
        self.draw_pieces(WIN)
        self.draw_validate(WIN)
        pygame.display.update()

    def select_piece(self, piece):
        piece.swicht_Select()
        self.get_valid_mov(piece)


