import unittest
from unittest.mock import patch

from app import start


class TestInit(unittest.TestCase):
    @patch('app.game.game.print')
    def test_init(self, mock_print):
        with patch('app.game.game.input', side_effect=('y', 'y', 'y', 'y', 'y')):
            start()
