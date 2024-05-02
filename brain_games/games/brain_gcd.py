#!/usr/bin/env python3

import random

game_rule = "Find the greatest common divisor of given numbers."

def gcd_game():
    remainder = 1
    first_number = random.randint(2, 100)
    second_number = random.randint(2, 100)
    question = f"{first_number} {second_number}"

    if first_number < second_number:
        first_number, second_number = second_number, first_number

    while remainder != 0:
        remainder = first_number % second_number
        first_number = second_number
        second_number = remainder

    
    correct_answer = first_number
    return(question, correct_answer)        



