import unittest
from app.pad650_ordem_decrescente import descending_order


class TestPad650(unittest.TestCase):

    def test_descending_order_test(self):
        self.assertEqual(descending_order(21445), 54421)
        self.assertEqual(descending_order(145263), 654321)
        self.assertEqual(descending_order(123456789), 987654321)
        self.assertEqual(descending_order(55896), 98655)
