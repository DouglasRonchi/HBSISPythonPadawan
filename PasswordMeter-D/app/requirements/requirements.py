from app.requirements.additions import Additions
from app.requirements.dedutions import Dedutions
from app.password.password import Password


class Requirements:
    def __init__(self, password: Password):
        self._password = password
        self._score = 0
        self._requirements = 0
        self.additions = Additions
        self.dedutions = Dedutions

    def get_score_validated(self):
        return self._score
