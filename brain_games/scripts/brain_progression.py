#!/usr/bin/env python3

from brain_games.engine import play_game
from brain_games.games.progression import progression_game, game_rule


def main():
    play_game(progression_game, game_rule)


if __name__ == '__main__':
    main()
