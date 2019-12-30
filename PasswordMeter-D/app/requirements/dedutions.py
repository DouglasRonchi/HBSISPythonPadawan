from app.requirements.requirements import Requirements, Password
from string import ascii_letters as alpha
import re


class Dedutions(Requirements):
    def __init__(self, password: Password):
        super().__init__(password)

    def validate(self):
        # Letters Only
        self._score -= self._verify_letters_only()

        # Numbers Only
        self._score -= self._verify_numbers_only()

        # Consecutive Uppercase Letters
        self._score -= self._verify_consecutive_uppercase_letters() * 2

        # Consecutive Lowercase Letters
        self._score -= self._verify_consecutive_lowercase_letters() * 2

        # Consecutive Numbers
        self._score -= self._verify_consecutive_numbers_on_password() * 2

        # Sequential Letters
        self._score -= self._verify_sequential_letters() * 3

        # Sequential Numbers
        self._score -= self._verify_sequential_numbers() * 3

        # Sequential Symbols
        self._score -= self._verify_sequential_symbols() * 3

        return self._score

    def _verify_letters_only(self) -> int:
        if len(re.findall('[a-zA-Z]', self._password.get_value())) == len(self._password.get_value()):
            return len(re.findall('[a-zA-Z]', self._password.get_value()))
        return 0

    def _verify_numbers_only(self) -> int:
        if len(re.findall('[\d]', self._password.get_value())) == len(self._password.get_value()):
            return len(re.findall('[\d]', self._password.get_value()))
        return 0

    def _verify_consecutive_uppercase_letters(self) -> int:
        return len(re.findall('[A-Z]{2}', self._password.get_value()))

    def _verify_consecutive_lowercase_letters(self) -> int:
        return len(re.findall('[a-z]{2}', self._password.get_value()))

    def _verify_consecutive_numbers_on_password(self) -> int:
        return len(re.findall('[\d]{2}', self._password.get_value()))

    def _verify_sequential_letters(self) -> int:
        passwd = []
        acertos = 0
        for caracter in self._password.get_value():
            try:
                passwd.append(alpha.index(caracter))
            except:
                passwd.append(caracter)
        for i in range(len(passwd)):
            if i == len(passwd) - 1:
                try:
                    if passwd[i - 1] == passwd[i] - 1:
                        acertos += 1
                except:
                    pass
            else:
                try:
                    if passwd[i] + 1 == passwd[i + 1]:
                        acertos += 1
                except:
                    pass
        if acertos >= 3:
            return acertos
        return 0

    def _verify_sequential_numbers(self) -> int:
        passwd = []
        acertos = 0
        for caracter in self._password.get_value():
            try:
                passwd.append(int(caracter))
            except:
                passwd.append(caracter)
            else:
                pass
        for i in range(len(passwd)):
            if i == len(passwd) - 1:
                try:
                    if passwd[i - 1] == passwd[i] - 1:
                        acertos += 1
                except:
                    pass
            else:
                try:
                    if passwd[i] + 1 == passwd[i + 1]:
                        acertos += 1
                except:
                    pass
        if acertos >= 3:
            return acertos
        return 0

    def _verify_sequential_symbols(self) -> int:
        passwd = []
        acertos = 0
        for caracter in self._password.get_value():
            passwd.append(caracter)
        for i in range(len(passwd)):
            if i == len(passwd) - 1:
                if len(re.findall('\W', passwd[i - 1])) > 0 and len(re.findall('\W', passwd[i])) > 0:
                    acertos += 1
            else:
                if len(re.findall('\W', passwd[i + 1])) > 0 and len(re.findall('\W', passwd[i])) > 0:
                    acertos += 1
        if acertos >= 3:
            return acertos
        return 0
