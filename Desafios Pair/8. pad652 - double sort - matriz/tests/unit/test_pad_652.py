import unittest
from app.pad652 import db_sort


class TestPad652(unittest.TestCase):

    def test_db_sort(self):
        self.assertEqual(db_sort(
            ["Banana", "Orange", "Apple", "Mango", 0, 2, 2]),
            [0, 2, 2, "Apple", "Banana", "Mango", "Orange"]
        )

        self.assertEqual(db_sort(
            ["Gol", "Fox", "Mercedez", 45, 10, 22, 21]),
            [10, 21, 22, 45, "Fox", "Gol", "Mercedez"]
        )

        self.assertEqual(db_sort(
            ["Goleiro", 14, "Meia", 55, "Atacante", 2, 2]),
            [2, 2, 14, 55, "Atacante", "Goleiro", "Meia"]
        )
