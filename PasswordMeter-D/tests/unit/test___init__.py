import unittest
from unittest.mock import patch

from app import start


class TestInit(unittest.TestCase):
    @patch('app.print')
    def test_if_start_really_start(self, mock_print):
        start()

