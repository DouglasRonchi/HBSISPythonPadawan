import unittest
from app.pad662 import teste_de_qi


class TestPad662(unittest.TestCase):

    def test_iq_test(self):
        self.assertEqual(teste_de_qi("2 4 7 8 10"), 3)
        self.assertEqual(teste_de_qi("1 1 1 1 1 2 1 1 1 3"), 6)
        self.assertEqual(teste_de_qi("1 1 1 1 1 2"), 6)
        self.assertEqual(teste_de_qi("2 1 2 2 2 2 2"), 2)
        self.assertEqual(teste_de_qi("0 0 2 2 1"), 5)
