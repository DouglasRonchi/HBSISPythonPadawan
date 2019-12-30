from random import shuffle


class Deck:
    def __init__(self, cards: list):
        self._cards = cards

    def get_cards(self):
        return self._cards.copy()

    def shuffle_deck(self):
        shuffle(self._cards)
        return self._cards.copy()

    def get_a_card(self):
        return self._cards.pop(0)


