import unittest

from app.tripulacao.tecnica.oficial import Oficial
from app.tripulacao.tripulante import Tripulante


class TestOficial(unittest.TestCase):
    def test_oficial_deveria_ter_um_nome_e_ser_um_tripulante(self):
        oficial = Oficial('Douglas')
        self.assertEqual(oficial.get_nome(), 'Douglas')
        self.assertIsInstance(oficial, Tripulante)


