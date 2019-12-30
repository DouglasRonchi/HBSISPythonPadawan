from app.password.password import Password
from app.requeriments.additions.additions import Additions
import re


class Symbols(Additions):
    def __init__(self, password: Password):
        super().__init__(password)

    def _get_number_of_symbols(self):
        contador = 0
        lista = re.findall('\W', self._password)
        for dado in lista:
            contador += 1
        return contador
