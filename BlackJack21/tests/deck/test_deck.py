import unittest
from unittest.mock import Mock

from app.deck.deck import Deck


class TestDeck(unittest.TestCase):
    def test_deck_should_be_a_instance_of_deck(self):
        entrada = Mock()
        deck = Deck(entrada)
        self.assertIsInstance(deck, Deck)

    def test_get_cards_should_return_a_copy_of_cards_list(self):
        #Arrange
        full_cards = []
        cards = [
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock()
        ]
        for i in range(4):
            for card in cards:
                full_cards.append(card)
        deck = Deck(full_cards)

        # Action
        action = deck.get_cards().copy()

        #Assert
        self.assertEqual(action, full_cards)

    def test_should_shuffle_cards_list(self):
        # Arrange
        cards = [
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock()
        ]
        initial_deck = cards.copy()
        deck = Deck(cards)

        # Action
        action = deck.shuffle_deck()
        # Assert
        assert action != initial_deck

    def test_if_get_a_card_pop_top_card_of_a_list(self):
        # Arrange
        cards = [
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock()
        ]
        deck = Deck(cards)

        # Action
        deck.get_a_card()

        # Assert
        remaining_cards = 12
        self.assertEqual(len(deck.get_cards()), remaining_cards)

    def test_if_get_a_card_pop_return_self_card(self):
        # Arrange
        cards = [
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock(),
            Mock()
        ]
        deck = Deck(cards)

        # Action
        action = deck.get_a_card()

        # Assert
        assert action not in deck.get_cards()
