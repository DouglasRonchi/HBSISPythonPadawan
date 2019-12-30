from app.password.password import Password
from app.requeriments.additions.additions import Additions


class NumberOfCharacters(Additions):
    def __init__(self, password: Password):
        super().__init__(password)

    def _get_numbers_of_characters(self):
        return len(self._password)
