import unittest
from app.pad649 import find_short


class TestPad649(unittest.TestCase):

    def test_find_short(self):
        self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
        self.assertEqual(find_short("maybe this code has some bugs"), 3)
        self.assertEqual(find_short("anytime anywhere"), 7)
        self.assertEqual(find_short("the next day will be better"), 2)
