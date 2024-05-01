#!/usr/bin/env python3

import random


game_rule = "What is the result of the expression?"

def calc_game():
    first_number = random.randint(2, 100)
    second_number = random.randint(2, 100)
    operation = random.randint(1, 3)
    if operation == 1:
        correct_answer = first_number + second_number
        question = f"{first_number} + {second_number}"
    elif operation == 2:
        correct_answer = first_number - second_number
        question = f"{first_number} - {second_number}"
    else:
        correct_answer = first_number * second_number
        question = f"{first_number} * {second_number}"
    return (question, correct_answer)


