from .tablero import Tablero
from .constantes import BLANCO, NEGRO


class Game:

    def __init__(self):
        
        self._init()
    
    def _init(self):
        self.tablero = Tablero()
        self.turno = BLANCO
        self.piece_selected = 0

    def restart(self):
        self._init()

    def draw(self, win):
        self.tablero.draw(win)

    def select(self, col, row):

        casilla = self.tablero.get_from_pos(col, row)
        
        if casilla != 0 and self.piece_selected == 0 and casilla.color == self.turno:
            self.piece_selected = casilla
            self.tablero.select_piece(casilla)
            self.tablero.get_valid_mov(casilla)
            return True

        elif casilla != 0 and self.piece_selected != 0 and casilla.color == self.turno:
            self.tablero.select_piece(self.piece_selected)
            self.piece_selected = casilla
            self.tablero.select_piece(casilla)
            self.tablero.get_valid_mov(casilla)
            return True

        elif self.piece_selected != 0 and casilla == 0 and self.tablero.is_Validate((col, row)):
            self.mov(self.piece_selected, col, row)
            self.piece_selected = 0
            self.tablero.restart_validate()
            self.change_turn()

        else:
            return False

    def mov(self, piece, col, row):
        self.tablero.mov(piece, col, row)

    def change_turn(self):
        if self.turno == BLANCO:
            self.turno = NEGRO
        else:
            self.turno = BLANCO

