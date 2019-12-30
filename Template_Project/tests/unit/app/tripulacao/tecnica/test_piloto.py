import unittest

from app.tripulacao.tecnica.piloto import Piloto
from app.tripulacao.tripulante import Tripulante


class TestPiloto(unittest.TestCase):
    def test_piloto_deveria_ter_um_nome_e_ser_um_tripulante(self):
        piloto = Piloto('Goku')
        self.assertEqual(piloto.get_nome(), 'Goku')
        self.assertIsInstance(piloto, Tripulante)
