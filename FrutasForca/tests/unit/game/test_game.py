import unittest
from unittest.mock import patch, Mock

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

    @patch('app.game.game.input')
    def test_trying_a_letter(self, mock_input):
        with patch('app.game.game.print'):
            mock_input.side_effect = ('a')
            game = Game()
            game.secret_fruit = Mock()
            game.secret_fruit.get_name.return_value = 'a'
            game.tip = ['__']
            result = game.trying_a_letter()
            self.assertEqual(result, ['A'])

    @patch('app.game.game.input')
    def test_trying_a_letter_that_not_in_secret_word(self, mock_input):
        with patch('app.game.game.print'):
            mock_input.side_effect = ('b')
            game = Game()
            game.secret_fruit = Mock()
            game.secret_fruit.get_name.return_value = 'a'
            game.tip = ['__']
            result = game.trying_a_letter()
            self.assertEqual(result, ['__'])

    def test_already_choice_same_letter(self):
        with patch('app.game.game.print'):
            game = Game()
            game.tip = ['A']
            result = game._already_choice_same_letter('a')
            self.assertEqual(result, True)

    def test_has_letter(self):
        game = Game()
        game.tip = ['A']
        game.secret_fruit = Mock()
        game.secret_fruit.get_name.return_value = 'a'
        result = game._has_letter('a')
        self.assertEqual(result, True)

    @patch('app.game.game.print')
    def test_start_game(self, mock_print):
        with patch('app.game.game.input', side_effect=('u', 'v', 'a')):
            game = Game()
            game.secret_fruit = Mock()
            game.secret_fruit.get_name.return_value = 'uva'
            game.tip = ["__", "__", "__"]
            game.start_game()
