from typing import Final

from app.fruits.bucket_of_fruits import BucketOfFruits

_HIDE_LETTER: Final = '__'


def _show(param):
    print(param)


def _get_input(param) -> str:
    return input(param)


class Game(BucketOfFruits):
    def __init__(self):
        super().__init__()
        self.tip = []
        self.chances = 5
        self.success = False

    def mount_tip(self) -> list:
        for position in range(self.secret_fruit.get_length()):
            self.tip.append(_HIDE_LETTER)
        return self.tip

    def trying_a_letter(self) -> list:
        self.success = False
        choice = _get_input('Write one letter: ')
        self._already_choice_same_letter(choice)
        self._has_letter(choice)
        if not self.success:
            self.chances -= 1
        return self.tip

    def _already_choice_same_letter(self, choice: str):
        if choice.upper() in self.tip:
            _show("You already tapped this letter!")
            self.chances -= 1
            return True

    def _has_letter(self, choice: str) -> bool:
        if choice in self.secret_fruit.get_name():
            count = 0
            for letter in self.secret_fruit.get_name():
                if choice == letter:
                    self.tip[count] = choice.upper()
                    self.success = True
                count += 1
            if self.success:
                return True

    def start_game(self) -> None:
        while self._not_lose():
            _show(self.tip)
            _show(f"Your Chances to miss: {self.chances}")
            self.trying_a_letter()
            if self._has_winner():
                _show('YOU WIN!')
                break
        _show(f"Tip: {self.tip}")
        _show(f"Secret Fruit: {self.secret_fruit.get_name()}")

    def _has_winner(self) -> bool:
        return _HIDE_LETTER not in self.tip

    def _not_lose(self) -> bool:
        return self.chances != 0
