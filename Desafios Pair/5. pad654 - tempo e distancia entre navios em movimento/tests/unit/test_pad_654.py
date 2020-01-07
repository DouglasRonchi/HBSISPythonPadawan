import unittest
from app.pad654 import find_time_to_break


class TestPad654(unittest.TestCase):

    def test_find_time_to_break(self):
        self.assertEqual(find_time_to_break(0, 90), 18.86)
