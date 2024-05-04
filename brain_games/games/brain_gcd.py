#!/usr/bin/env python3

import random


game_rule = "Find the greatest common divisor of given numbers."


def gcd(first_number, second_number):
    remainder = 1

    if first_number < second_number:
        first_number, second_number = second_number, first_number

    while remainder != 0:
        remainder = first_number % second_number
        first_number = second_number
        second_number = remainder
    return first_number


def gcd_game():

    first_number = random.randint(2, 100)
    second_number = random.randint(2, 100)
    question = f"{first_number} {second_number}"

    correct_answer = gcd(first_number, second_number)
    return (question, correct_answer)
