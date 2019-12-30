import unittest

from app.tripulacao.cabine.chefe_de_servico import ChefeDeServico
from app.tripulacao.tripulante import Tripulante


class TestChefeDeServico(unittest.TestCase):
    def test_chefe_de_servico_deveria_ter_um_nome_e_ser_um_tripulante(self):
        # Arrange
        nome = 'Chefe'

        # Action
        chefe_de_servico = ChefeDeServico(nome)

        # Assertions
        self.assertEqual(chefe_de_servico.get_nome(), nome)
        self.assertIsInstance(chefe_de_servico, Tripulante)
