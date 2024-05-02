import random


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_game():
    number = random.randint(2, 200)
    question = number

    divider = 2
    while number % divider != 0:
        divider += 1
    if divider == number:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (question, correct_answer)
