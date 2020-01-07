import unittest
from app.pad651 import square_digits


class TestPad651(unittest.TestCase):

    def test_square_digits(self):
        self.assertEqual(square_digits(9119), 811181)
        self.assertEqual(square_digits(91), 811)
        self.assertEqual(square_digits(89), 6481)
        self.assertEqual(square_digits(48), 1664)
