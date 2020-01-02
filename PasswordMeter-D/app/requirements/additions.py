import re

from termcolor import colored

from app.password.password import Password
from app.requirements.requirements import Requirements


class Additions(Requirements):
    def __init__(self, password: Password):
        super().__init__(password)

    def show_addition_references(self):
        print(colored(f"{'ADDITIONS':^38}", 'blue'))
        characters = self._verify_numbers_of_characters()
        numbers = self._verify_numbers_on_password()
        upper = self._verify_uppercase_letters()
        lower = self._verify_lowercase_letters()
        symbols = self._verify_symbols_on_password()
        num_symbols = self._verify_middle_numbers_and_symbols()
        print(f"{'Category':.<30} {'qtd':>2}:{'vlr'}")
        print(f"{'Number of Characters:':.<30} {characters['count']:>2} = {characters['value']}")
        print(f"{'Number of Numbers:':.<30} {numbers['count']:>2} = {numbers['value']}")
        print(f"{'Number of UpperCase:':.<30} {upper['count']:>2} = {upper['value']}")
        print(f"{'Number of LowerCase:':.<30} {lower['count']:>2} = {lower['value']}")
        print(f"{'Number of Symbols:':.<30} {symbols['count']:>2} = {symbols['value']}")
        print(f"{'Middle Numbers and Symbols:':.<30} {num_symbols['count']:>2} = {num_symbols['value']}")
        print(f"{'Requeriments:':.<30} {self._requirements:>2} = {self._requirements * 2}")

    def validate(self):
        # Number of Characters
        characters = self._verify_numbers_of_characters()
        self._score += characters['value']

        # Uppercase letters and Lowercase Letters and numbers
        maiusculas = self._verify_uppercase_letters()
        minusculas = self._verify_lowercase_letters()
        numeros = self._verify_numbers_on_password()
        if 0 < numeros['count'] < len(self._password.get_value()):
            self._score += numeros['count']
            if maiusculas['count'] > 0 and minusculas['count'] > 0:
                self._score += maiusculas['value']
                self._score += minusculas['value']
            elif maiusculas['count'] > 0 or minusculas['count'] > 0:
                if maiusculas['count'] > 0:
                    self._score += maiusculas['value']
                else:
                    self._score += minusculas['value']
        if numeros['count'] > 0 and maiusculas['count'] > 0 and minusculas['count'] > 0:
            self._requirements += 1

        # Symbols
        symbols = self._verify_symbols_on_password()
        self._score += symbols['value']

        # Middle Numbers And Symbols
        numbers_symbols = self._verify_middle_numbers_and_symbols()
        self._score += numbers_symbols['value']

        # Requirements
        if self._requirements > 3 and characters['count'] >= 8:
            self._score += self._requirements * 2
        return self._score

    def _verify_numbers_of_characters(self) -> dict:
        lista = {}
        if len(self._password.get_value()) >= 8:
            self._requirements += 1
        lista['count'] = len(self._password.get_value())
        lista['value'] = len(self._password.get_value()) * 4
        return lista

    def _verify_uppercase_letters(self) -> dict:
        contador = 0
        uppercase = {}
        for dado in re.findall('[A-Z]+', self._password.get_value()):
            contador += len(dado)
        uppercase['count'] = contador
        uppercase['value'] = (len(self._password.get_value()) - contador) * 2
        return uppercase

    def _verify_lowercase_letters(self) -> dict:
        lista = {}
        contador = 0
        for dado in re.findall('[a-z]+', self._password.get_value()):
            contador += len(dado)
        lista['count'] = contador
        lista['value'] = (len(self._password.get_value()) - contador) * 2
        return lista

    def _verify_numbers_on_password(self) -> dict:
        lista = {}
        contador = len(re.findall('\d', self._password.get_value()))
        lista['count'] = contador
        lista['value'] = contador * 4
        return lista

    def _verify_symbols_on_password(self) -> dict:
        lista = {}
        if len(re.findall('\W', self._password.get_value())) > 0:
            self._requirements += 1
        contador = len(re.findall('\W', self._password.get_value()))
        lista['count'] = contador
        lista['value'] = contador * 6
        return lista

    def _verify_middle_numbers_and_symbols(self) -> dict:
        lista = {}
        contador = 0
        comeco = 1
        final = int(len(self._password.get_value()) - 1)
        contador += len(re.findall('\d', self._password.get_value()[comeco:final]))
        contador += len(re.findall('\W', self._password.get_value()[comeco:final]))
        if contador > 0:
            self._requirements += 1
        lista['count'] = contador
        lista['value'] = contador * 2
        return lista

