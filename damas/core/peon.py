from damas.core.constantes import NEGRO, BLANCO

class Peon:

    def __init__(self, columna, fila):
        
        self.columna = columna
        self.fila = fila
        self.reina = False
        self.color = self.color_init()

    def soy_reina(self):
        self.reina = True

    def mover(self, columna, fila):
        self.fila = fila
        self.columna = columna

    def color_init(self):
        if self.fila < 4:
            return NEGRO
        else:
            return BLANCO

    def __repr__(self):
        return self.color

    def __str__(self):
        return f'Peon {self.color} POS{self.columna},{self.fila}'