import unittest
from unittest.mock import Mock

from app import Frutas


class TestFrutas(unittest.TestCase):
    def test_se_fruta_e_uma_instancia_da_classe_frutas(self):
        lista = Mock()
        fruta = Frutas(lista)
        self.assertIsInstance(fruta, Frutas)


