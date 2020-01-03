from random import choice

from app.fruits.fruit import Fruit


class BucketOfFruits:
    def __init__(self):
        self.list_of_fruits = [
            Fruit('morango'),
            Fruit('banana'),
            Fruit('mirtilo'),
            Fruit('pitanga'),
            Fruit('abacaxi'),
            Fruit('jabuticaba'),
            Fruit('maracuja'),
            Fruit('manga'),
            Fruit('uva'),
            Fruit('jaca'),
            Fruit('cereja')
        ]
        self.secret_fruit = Fruit

    def get_a_random_fruit(self) -> object:
        fruit = choice(self.list_of_fruits)
        self.secret_fruit = fruit
        return fruit
