import unittest
from damas.core.constantes import BLANCO, NEGRO
from damas.core.peon import Peon

class TestCasePeon(unittest.TestCase):

    def test_Peon_Crear(self):
        negro = Peon(0, 2)
        blanco = Peon(0, 5)
        self.assertEqual(repr(blanco.color), f'{BLANCO}')
        self.assertEqual(repr(negro.color), f'{NEGRO}')

    def test_Peon_Mover(self):
        peon = Peon(0, 0)
        peon.mover(4, 3)
        self.assertEqual(peon.col, 4)
        self.assertEqual(peon.row, 3)

    def test_Peon_mover_para_queen(self):
        pass
    