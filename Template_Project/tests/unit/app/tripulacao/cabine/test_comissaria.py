import unittest

from app.tripulacao.cabine.comissaria import Comissaria
from app.tripulacao.tripulante import Tripulante


class TestComissaria(unittest.TestCase):
    def test_comissaria_deveria_ter_um_nome_e_ser_um_tripulante(self):
        comissaria = Comissaria('Comissaria')
        self.assertEqual(comissaria.get_nome(), 'Comissaria')
        self.assertIsInstance(comissaria, Tripulante)
