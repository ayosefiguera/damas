import unittest
from damas.core.constantes import BLANCO, NEGRO, colS, rowS
from damas.core.peon import Peon
from damas.core.tablero import Tablero

class TestCaseTablero(unittest.TestCase):

    def test_Tablero_initiate(self):
        tablero = Tablero()
        self.assertEqual(len(tablero.tablero), colS)
        for col in range(colS):
            self.assertEqual(len(tablero.tablero[col]), colS)