import unittest
from damas.core.constantes import BLANCO, NEGRO, COLUMNAS, FILAS
from damas.core.peon import Peon
from damas.core.tablero import Tablero

class TestCaseTablero(unittest.TestCase):

    def test_Tablero_inizializar(self):
        tablero = Tablero()
        self.assertEqual(len(tablero.tablero), COLUMNAS)
        for col in range(COLUMNAS):
            self.assertEqual(len(tablero.tablero[col]), COLUMNAS)