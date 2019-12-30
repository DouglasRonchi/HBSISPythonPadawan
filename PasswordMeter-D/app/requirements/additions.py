from app.requirements.requirements import Requirements, Password
import re


class Additions(Requirements):
    def __init__(self, password: Password):
        super().__init__(password)

    def validate(self):
        # Number of Characters
        characters = self._verify_numbers_of_characters()
        self._score += characters * 4

        # Uppercase letters and Lowercase Letters
        maiusculas = self._verify_uppercase_letters()
        minusculas = self._verify_lowercase_letters()
        if maiusculas > 0 and minusculas > 0:
            self._score += (len(self._password.get_value()) - maiusculas) * 2
            self._score += (len(self._password.get_value()) - minusculas) * 2
            self._requirements += 1

        # numbers
        self._score += self._verify_numbers_on_password() * 4

        # Symbols
        self._score += self._verify_symbols_on_password() * 6

        # Middle Numbers And Symbols
        self._score += self._verify_middle_numbers_and_symbols() * 2

        # Requirements
        if self._requirements > 3 and characters >= 8:
            self._score += self._requirements * 2

        return self._score

    def _verify_numbers_of_characters(self) -> int:
        if len(self._password.get_value()) >= 8:
            self._requirements += 1
        return len(self._password.get_value())

    def _verify_uppercase_letters(self) -> int:
        contador = 0
        for dado in re.findall('[A-Z]+', self._password.get_value()):
            contador += len(dado)
        return contador

    def _verify_lowercase_letters(self) -> int:
        contador = 0
        for dado in re.findall('[a-z]+', self._password.get_value()):
            contador += len(dado)
        return contador

    def _verify_numbers_on_password(self) -> int:
        if len(re.findall('\d', self._password.get_value())) > 0:
            self._requirements += 1
        return len(re.findall('\d', self._password.get_value()))

    def _verify_symbols_on_password(self) -> int:
        if len(re.findall('\W', self._password.get_value())) > 0:
            self._requirements += 1
        return len(re.findall('\W', self._password.get_value()))

    def _verify_middle_numbers_and_symbols(self) -> int:
        contador = 0
        comeco = 1
        final = int(len(self._password.get_value()) - 1)
        contador += len(re.findall('\d', self._password.get_value()[comeco:final]))
        contador += len(re.findall('\W', self._password.get_value()[comeco:final]))
        if contador > 0:
            self._requirements += 1
        return contador
