import unittest

from app.fruits.fruit import Fruit


class TestFruit(unittest.TestCase):
    def test_if_fruit_is_a_instance_of_fruit(self):
        fruit = Fruit('morango')
        self.assertIsInstance(fruit, Fruit)

    def test_get_name(self):
        fruit = Fruit('morango')
        fruit_name = fruit.get_name()
        self.assertEqual(fruit_name, 'morango')

    def test_get_length(self):
        fruit = Fruit('morango')
        fruit_length = fruit.get_length()
        self.assertEqual(fruit_length, 7)

    def test_if_new_str_return_correctly(self):
        fruit = Fruit('morango')
        self.assertEqual(fruit.__str__(), 'Name: Morango - Length: 7')