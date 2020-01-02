import unittest

from app import start


class TestInit(unittest.TestCase):
    def test_init(self):
        start()

