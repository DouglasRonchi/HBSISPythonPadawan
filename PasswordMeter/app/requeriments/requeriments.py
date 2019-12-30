from app.password.password import Password
from app.rate.rate import Rate
from app.requeriments.additions.number_of_characters import NumberOfCharacters


class Requeriment:
    def __init__(self, password: Password):
        self._password = password
        self._rate = Rate
        self.number_of_chars = NumberOfCharacters
