from app.game.game import Game


def start():
    game = Game()
    game.get_a_random_fruit()
    game.mount_tip()
    game.start_game()
