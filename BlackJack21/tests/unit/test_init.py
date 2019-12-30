import unittest
from unittest.mock import patch

from app import start


class TestInit(unittest.TestCase):
    @patch('app.deck.blackjack.sleep')
    @patch('app.deck.blackjack.print')
    @patch('app.deck.blackjack.input')
    def test_if_init_works(self, mock_input, mock_print, mock_sleep):
        start()

