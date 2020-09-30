from .tablero import Tablero
from .constantes import BLANCO, NEGRO


class Game:

    def __init__(self):
        
        self._init()
    
    def _init(self):
        self.tablero = Tablero()
        self.turno = BLANCO
        self.pieza_seleccionada = 0

    def restart(self):
        self._init()

    def draw(self, win):
        self.tablero.draw(win)

    def select(self, col, fila):

        casilla = self.tablero.get_from_pos(col, fila)
        
        if casilla != 0 and self.pieza_seleccionada == 0 and casilla.color == self.turno:
            self.pieza_seleccionada = casilla
            self.tablero.select_piece(casilla)
            self.tablero.get_valid_mov(casilla)
            return True

        elif casilla != 0 and self.pieza_seleccionada != 0 and casilla.color == self.turno:
            self.tablero.select_piece(self.pieza_seleccionada)
            self.pieza_seleccionada = casilla
            self.tablero.select_piece(casilla)
            self.tablero.get_valid_mov(casilla)
            return True

        elif self.pieza_seleccionada != 0 and casilla == 0 and self.tablero.is_Validate((col, fila)):
            self.mov(self.pieza_seleccionada, col, fila)
            self.pieza_seleccionada = 0
            self.tablero.restart_validate()
            self.change_turn()

        else:
            return False

    def mov(self, pieza, col, fila):
        self.tablero.mov(pieza, col, fila)

    def change_turn(self):
        if self.turno == BLANCO:
            self.turno = NEGRO
        else:
            self.turno = BLANCO

