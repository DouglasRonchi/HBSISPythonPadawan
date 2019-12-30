from app.password.password import Password
from app.requeriments.additions.additions import Additions
import re


class Numbers(Additions):
    def __init__(self, password: Password):
        super().__init__(password)

    def _get_number_of_numbers_on_password(self):
        contador = 0
        lista = re.findall('\d', self._password)
        for dado in lista:
            contador += 1
        return contador
