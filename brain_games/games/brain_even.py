#!/usr/bin/env python3


import random


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_game():
    number = random.randint(1, 100)
    if number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (number, correct_answer)
