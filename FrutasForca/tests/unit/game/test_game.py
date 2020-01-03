import unittest

from app import Game


class TestGame(unittest.TestCase):
    def test_if_game_is_a_instance_of_game_class(self):
        game = Game()
        self.assertIsInstance(game, Game)

    def test_mount_a_tip(self):
        game = Game()
        game.get_a_random_fruit()
        fruit_tip = game.mount_tip()
        fruit_name = game.secret_fruit.get_name()
        self.assertEqual(len(fruit_tip), len(fruit_name))
