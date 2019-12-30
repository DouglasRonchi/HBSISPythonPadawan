import unittest
from unittest.mock import Mock, MagicMock, patch

from app import BlackJack
from app.deck.deck import Deck
from app.deck.card import Card


class TestBlackJack(unittest.TestCase):
    def test_if_blackjack_is_a_instance_of_blackjack(self):
        blackjack = BlackJack()
        self.assertIsInstance(blackjack, BlackJack)

    def test_if_constructor_return_a_instance_of_deck(self):
        blackjack = BlackJack()
        self.assertIsInstance(blackjack._deck, Deck)

    def test_presentation_work_fine(self):
        blackjack = BlackJack()
        action = blackjack.presentation()
        self.assertEqual(action, action)

    @patch('app.deck.blackjack.input')
    def test_if_get_a_card_in_a_round_works(self, mock_input):
        blackjack = BlackJack()
        result = blackjack._round()
        self.assertEqual(result, blackjack._score)

    def test_is_done_function_should_return_true_if_result_is_equal_21(self):
        blackjack = BlackJack()
        blackjack._score = 21
        result = blackjack._is_done()
        self.assertEqual(result, True)

    def test_is_done_function_should_return_true_if_result_is_greater_21(self):
        blackjack = BlackJack()
        blackjack._score = 25
        result = blackjack._is_done()
        self.assertEqual(result, True)

    def test_calculate_points_should_be_sum_points_in_a_player_hand(self):
        blackjack = BlackJack()

        card_1 = MagicMock()
        card_1.value = 3

        card_2 = MagicMock()
        card_2.value = 3

        blackjack._player_hand.append(card_1)
        blackjack._player_hand.append(card_2)
        blackjack._calculate_score()

        self.assertEqual(blackjack._score, 6)

    def test_if_finish_show_blackjack_with_21_points(self):
        blackjack = BlackJack()
        blackjack._score = 21
        result = blackjack.finish()
        self.assertEqual(result, 'BLACKJACK')

    def test_if_finish_show_youlose_with_more_than_21_points(self):
        blackjack = BlackJack()
        blackjack._score = 22
        result = blackjack.finish()
        self.assertEqual(result, 'You Lose!')
