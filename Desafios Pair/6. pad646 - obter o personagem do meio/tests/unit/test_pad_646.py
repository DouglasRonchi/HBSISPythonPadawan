import unittest
from app.pad646 import get_middle


class TestPad646(unittest.TestCase):

    def test_get_middle(self):
        self.assertEqual(get_middle("self"), "el")
        self.assertEqual(get_middle("selfing"), "f")
        self.assertEqual(get_middle("middle"), "dd")
        self.assertEqual(get_middle("A"), "A")
        self.assertEqual(get_middle("of"), "of")
        self.assertEqual(get_middle("Douglas"), "g")
        self.assertEqual(get_middle("hbsis"), "s")
        self.assertEqual(get_middle("padawan"), "a")
