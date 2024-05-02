from brain_games.engine import play_game
from brain_games.games.brain_gcd import gcd_game, game_rule


def main():
    play_game(gcd_game, game_rule)


if __name__ == '__main__':
    main()
