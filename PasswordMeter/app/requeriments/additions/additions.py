from app.password.password import Password
from app.requeriments.requeriments import Requeriment


class Additions(Requeriment):
    def __init__(self, password: Password):
        super().__init__(password)
        self._bonus = 0

    def get_bonus(self):
        return self._bonus

    def set_bonus(self, bonus):
        self._bonus = bonus
