import random


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    if divider == number:
        return True
    else:
        return False


def prime_game():
    number = random.randint(2, 200)
    question = number

    correct_answer = "yes" if is_prime(number) else "no"

    return (question, correct_answer)
