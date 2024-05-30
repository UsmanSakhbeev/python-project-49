#!/usr/bin/env python3

from brain_games.engine import play_game
from brain_games.games.brain_prime import prime_game, game_rule


def main():
    play_game(prime_game, game_rule)


if __name__ == '__main__':
    main()
