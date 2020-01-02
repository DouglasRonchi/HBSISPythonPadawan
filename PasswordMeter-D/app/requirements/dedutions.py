import re
from string import ascii_letters as alpha

from termcolor import colored

from app.password.password import Password
from app.requirements.requirements import Requirements


class Dedutions(Requirements):
    def __init__(self, password: Password):
        super().__init__(password)

    def show_dedution_references(self):
        print(colored(f"{'DEDUTIONS':^38}", 'red'))
        letters = self._verify_letters_only()
        numbers = self._verify_numbers_only()
        cons_upper = self._verify_consecutive_uppercase_letters()
        cons_lower = self._verify_consecutive_lowercase_letters()
        cons_numb = self._verify_consecutive_numbers_on_password()
        seq_letters = self._verify_sequential_letters()
        seq_numbers = self._verify_sequential_numbers()
        seq_symbols = self._verify_sequential_symbols()
        print(f"{'Category':.<30} {'qtd':>2}:{'vlr'}")
        print(f"{'Letters Only:':.<30} {letters['count']:>2} = {letters['value']}")
        print(f"{'Numbers Only:':.<30} {numbers['count']:>2} = {numbers['value']}")
        print(f"{'Consecutive UpperCase:':.<30} {cons_upper['count']:>2} = {cons_upper['value']}")
        print(f"{'Consecutive LowerCase:':.<30} {cons_lower['count']:>2} = {cons_lower['value']}")
        print(f"{'Consecutive Numbers:':.<30} {cons_numb['count']:>2} = {cons_numb['value']}")
        print(f"{'Sequential Letters:':.<30} {seq_letters['count']:>2} = {seq_letters['value']}")
        print(f"{'Sequential Numbers:':.<30} {seq_numbers['count']:>2} = {seq_numbers['value']}")
        print(f"{'Sequential Symbols:':.<30} {seq_symbols['count']:>2} = {seq_symbols['value']}")

    def validate(self):
        # Letters Only
        letters = self._verify_letters_only()
        self._score -= letters['value']

        # Numbers Only
        numbers = self._verify_numbers_only()
        self._score -= numbers['value']

        # Consecutive Uppercase Letters
        conseq_upper = self._verify_consecutive_uppercase_letters()
        self._score -= conseq_upper['value']

        # Consecutive Lowercase Letters
        conseq_lower = self._verify_consecutive_lowercase_letters()
        self._score -= conseq_lower['value']

        # Consecutive Numbers
        conseq_numbers = self._verify_consecutive_numbers_on_password()
        self._score -= conseq_numbers['value']

        # Sequential Letters
        seq_letters = self._verify_sequential_letters()
        self._score -= seq_letters['value']

        # Sequential Numbers
        seq_numbers = self._verify_sequential_numbers()
        self._score -= seq_numbers['value']

        # Sequential Symbols
        seq_symbols = self._verify_sequential_symbols()
        self._score -= seq_symbols['value']

        return self._score

    def _verify_letters_only(self) -> dict:
        lista = {}
        if len(re.findall('[a-zA-Z]', self._password.get_value())) == len(self._password.get_value()):
            lista['count'] = len(re.findall('[a-zA-Z]', self._password.get_value()))
            lista['value'] = len(re.findall('[a-zA-Z]', self._password.get_value()))
            return lista
        lista['count'] = 0
        lista['value'] = 0
        return lista

    def _verify_numbers_only(self) -> dict:
        lista = {}
        if len(re.findall('[\d]', self._password.get_value())) == len(self._password.get_value()):
            lista['count'] = len(re.findall('[\d]', self._password.get_value()))
            lista['value'] = len(re.findall('[\d]', self._password.get_value()))
            return lista
        lista['count'] = 0
        lista['value'] = 0
        return lista

    def _verify_consecutive_uppercase_letters(self) -> dict:
        lista = {}
        consecutive = 0
        password = self._password.get_value()
        for i in range(len(password) - 1):
            if i != (len(password)):
                if password[i].isupper():
                    if password[i + 1].isupper():
                        consecutive += 1
        lista['count'] = consecutive
        lista['value'] = consecutive * 2
        return lista

    def _verify_consecutive_lowercase_letters(self) -> dict:
        lista = {}
        consecutive = 0
        password = self._password.get_value()
        for i in range(len(password) - 1):
            if i != (len(password)):
                if password[i].islower():
                    if password[i + 1].islower():
                        consecutive += 1
        lista['count'] = consecutive
        lista['value'] = consecutive * 2
        return lista

    def _verify_consecutive_numbers_on_password(self) -> dict:
        lista = {}
        consecutive = 0
        password = self._password.get_value()
        for i in range(len(password) - 1):
            if i != (len(password)):
                if password[i].isnumeric():
                    if password[i + 1].isnumeric():
                        consecutive += 1
        lista['count'] = consecutive
        lista['value'] = consecutive * 2
        return lista

    def _verify_sequential_letters(self) -> dict:
        lista = {}
        passwd = self._password.get_value()
        consecutive = 0
        for i in range(len(passwd) - 1):
            if i != (len(passwd)):
                try:
                    if alpha.index(passwd[i]) == int(alpha.index(passwd[i + 1]) - 1):
                        consecutive += 1
                except:
                    pass
        if consecutive < 1:
            lista['count'] = 0
            lista['value'] = 0
            return lista
        lista['count'] = consecutive - 1
        lista['value'] = (consecutive - 1) * 3
        return lista

    def _verify_sequential_numbers(self) -> dict:
        lista = {}
        passwd = self._password.get_value()
        consecutive = 0
        for i in range(len(passwd) - 1):
            if i != (len(passwd)):
                try:
                    if int(passwd[i]) == int(passwd[i + 1]) - 1:
                        consecutive += 1
                except:
                    pass
        if consecutive < 1:
            lista['count'] = 0
            lista['value'] = 0
            return lista
        lista['count'] = consecutive - 1
        lista['value'] = (consecutive - 1) * 3
        return lista

    def _verify_sequential_symbols(self) -> dict:
        lista = {}
        passwd = []
        acertos = 0
        consecutivas = 0
        for caracter in self._password.get_value():
            passwd.append(caracter)
        for i in range(len(passwd)):
            if i != len(passwd):
                if len(re.findall('\W', passwd[i - 1])) > 0 and len(re.findall('\W', passwd[i])) > 0:
                    acertos += 1
                    if acertos >= 3:
                        consecutivas += 1
        lista['count'] = consecutivas
        lista['value'] = consecutivas * 3
        return lista
