from time import sleep

from app.deck.card import Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, J, Q, K
from app.deck.deck import Deck


class BlackJack(object):
    def __init__(self):
        full_cards = []
        cards = [
            Ace(),
            Two(),
            Three(),
            Four(),
            Five(),
            Six(),
            Seven(),
            Eight(),
            Nine(),
            Ten(),
            J(),
            Q(),
            K()
        ]
        for i in range(4):
            for card in cards:
                full_cards.append(card)

        self._deck = Deck(full_cards)
        self._player_hand = []
        self._score = 0

    def play(self):
        while self._score < 21:
            self._deck.shuffle_deck()
            self._round()
            if self._is_done():
                self.finish()

    def presentation(self):
        print("="*55)
        print(f"{'BlackJack'::^55}")
        print("="*55)

    def _round(self):
        input("Aperte enter para virar uma carta...")
        card = self._deck.get_a_card()
        self._player_hand.append(card)
        self._calculate_score(card)
        print(f"Você virou a carta {card.name}")
        print(f"Pontuação: {self._score}")

    def _is_done(self):
        if self._score >= 21:
            return True

    def _calculate_score(self, card):
        self._score = sum(map(lambda card: card.value, self._player_hand))

    def finish(self):
        print("Calculando", end="")
        sleep(0.5)
        print(".", end="")
        sleep(0.5)
        print(".", end="")
        sleep(0.5)
        print(".", end="")
        sleep(0.5)
        print("")
        mensagem = "BLACKJACK" if self._score == 21 else "Você Perdeu..."

        print("-" * 55)
        print(f"{mensagem::^55}")
        print("-" * 55)
        print(f"Pontuação total: {self._score}")



