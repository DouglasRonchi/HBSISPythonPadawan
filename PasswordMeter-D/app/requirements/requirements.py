from termcolor import colored

from app.password.password import Password


class Requirements:
    def __init__(self, password: Password):
        self._password = password
        self._score = 0
        self._requirements = 0

    def get_score_validated(self):
        return self._score

    def show_score_total_points(self):
        if self._score > 100:
            rate = '100 %'
        else:
            rate = str(self._score) + " %"

        if self._score < 50:
            print(colored(f"{'TOTAL':^38}", 'red'))
            print(colored(f"{'Password: '}{self._password.get_value()}", 'red'))
            print(colored(f"{rate:^38}", 'red'))
        else:
            print(colored(f"{'TOTAL':^38}", 'green'))
            print(colored(f"{'Password: '}{self._password.get_value()}", 'green'))
            print(colored(f"{rate:^38}", 'green'))

