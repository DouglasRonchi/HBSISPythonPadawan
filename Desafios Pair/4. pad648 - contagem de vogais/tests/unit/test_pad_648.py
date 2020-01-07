import unittest
from app.pad648 import vowel_count


class TestPad648(unittest.TestCase):

    def test_vowel_count(self):
        self.assertEqual(vowel_count("abracadabra"), 5)
        self.assertEqual(vowel_count("harry potter"), 3)
        self.assertEqual(vowel_count("badword"), 2)
        self.assertEqual(vowel_count("alakasan"), 4)
