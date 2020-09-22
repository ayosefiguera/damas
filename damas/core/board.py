import pygame
from .setup import BLACK, ROWS, COLS, RED, SQUARE_SIZE, WHITE
from .piece import Piece



class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_queen = self.white_queen = 0
        self.inizialite_board()

    def draw_damero(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE,
                                    col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def get_piece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        self.board[row][col] = self.board[piece.row][piece.col]        
        self.board[piece.row][piece.col] = 0
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            print('Sere reina')
            piece.be_queen()
            if piece.color == WHITE:
                self.white_queen += 1
            else:
                self.red_queen += 1
    
    def inizialite_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_damero(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
