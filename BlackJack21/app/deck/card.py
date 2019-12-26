class Card:
    def __init__(self, name: str, value: int):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Ace(Card):
    def __init__(self, name='A', value=1):
        super().__init__(name, value)


class Two(Card):
    def __init__(self, name='2', value=2):
        super().__init__(name, value)


class Three(Card):
    def __init__(self, name='3', value=3):
        super().__init__(name, value)


class Four(Card):
    def __init__(self, name='4', value=4):
        super().__init__(name, value)


class Five(Card):
    def __init__(self, name='5', value=5):
        super().__init__(name, value)


class Six(Card):
    def __init__(self, name='6', value=6):
        super().__init__(name, value)


class Seven(Card):
    def __init__(self, name='7', value=7):
        super().__init__(name, value)


class Eight(Card):
    def __init__(self, name='8', value=8):
        super().__init__(name, value)


class Nine(Card):
    def __init__(self, name='9', value=9):
        super().__init__(name, value)


class Ten(Card):
    def __init__(self, name='10', value=10):
        super().__init__(name, value)


class J(Card):
    def __init__(self, name='J', value=10):
        super().__init__(name, value)


class Q(Card):
    def __init__(self, name='Q', value=10):
        super().__init__(name, value)


class K(Card):
    def __init__(self, name='K', value=10):
        super().__init__(name, value)
