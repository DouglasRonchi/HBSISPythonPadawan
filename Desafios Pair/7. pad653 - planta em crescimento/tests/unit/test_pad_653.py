import unittest
from app.pad653 import Plant


class TestPad653(unittest.TestCase):

    def test_growing_plant(self):
        plant = Plant()
        self.assertEqual(plant.growing_plant(100, 10, 910), 10)
        self.assertEqual(plant.growing_plant(10, 9, 4), 1)
        self.assertEqual(plant.growing_plant(50, 10, 500), 13)
