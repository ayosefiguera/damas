import pygame
from .tablero import Tablero
from .constantes import BLANCO, NEGRO, WIDTH, HEIGHT, BLACK_TURN, WHITE_TURN
from time import sleep

class Game:

    def __init__(self, win):
        self.win = win
        self._init()
    
    def _init(self):
        self.tablero = Tablero()
        self.turno = BLANCO
        self.piece_selected = 0

    def selected(self, piece):
        self.piece_selected = piece
        self.tablero.select_piece(piece)

    def restart(self):
        self._init()

    def draw(self):
        self.tablero.draw(self.win)

    def select(self, col, row):

        casilla = self.tablero.get_from_pos(col, row)
        
        if casilla != 0 and self.piece_selected == 0 and casilla.color == self.turno:
            self.selected(casilla)
            return True

        elif casilla != 0 and self.piece_selected != 0 and casilla.color == self.turno:
            self.selected(casilla)
            return True

        elif self.piece_selected != 0 and casilla == 0 and self.tablero.is_Validate((col, row)):
            self.mov(self.piece_selected, col, row)
            self.is_winner()
            self.change_turn()
            self.draw()
            self.on_draw_turn()

        else:
            return False

    def is_winner(self):
        winner = self.tablero.winner()
        if winner:
            self.on_draw_winner(winner)
        else:    
            return False

    def mov(self, piece, col, row):
        self.tablero.mov(piece, col, row)

    def on_draw_turn(self):
        if self.turno == NEGRO:
            turn = BLACK_TURN
        else:
            turn = WHITE_TURN

        self.win.blit(turn, ((WIDTH - turn.get_width())//2, (HEIGHT - turn.get_height())//2))
        pygame.display.flip()
        sleep(0.5)
    
    def on_draw_winner(self, winner):
        self.win.blit(winner, ((WIDTH - winner.get_width() )//
                               2, (HEIGHT - winner.get_height()) // 2))
        pygame.display.flip()
        sleep(2)

    def change_turn(self):

        self.piece_selected = 0
        self.tablero.restart_validate()
        if self.turno == BLANCO:
            self.turno = NEGRO
        else:
            self.turno = BLANCO

       
