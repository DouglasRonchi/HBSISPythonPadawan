import unittest
from app.pad647_resmungando import accum


class TestPad647(unittest.TestCase):

    def test_accum(self):
        self.assertEqual(
            accum("ZpglnRxqenU"),
            "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
        )
        self.assertEqual(
            accum("abcD"),
            "A-Bb-Ccc-Dddd"
        )
        self.assertEqual(
            accum("azhu"),
            "A-Zz-Hhh-Uuuu"
        )
        self.assertEqual(
            accum("kieu"),
            "K-Ii-Eee-Uuuu"
        )
