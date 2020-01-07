import unittest
from app.pad653 import growing_plant


class TestPad653(unittest.TestCase):

    def test_growing_plant(self):
        self.assertEqual(growing_plant(100, 10, 910), 10)
        self.assertEqual(growing_plant(10, 9, 4), 1)
        self.assertEqual(growing_plant(50, 10, 500), 13)
