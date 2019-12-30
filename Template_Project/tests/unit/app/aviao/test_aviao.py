import unittest

from app.aviao.aviao import Aviao


class TestAviao(unittest.TestCase):
    def test_aviao_nao_deveria_ter_passageiros(self):
        aviao = Aviao()
        self.assertEqual(len(aviao.get_passageiros()), 0)
