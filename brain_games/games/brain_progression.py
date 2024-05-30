import random


game_rule = "What number is missing in the progression?"


def create_progression(current_number, step, length):
    return [current_number + i * step for i in range(length)]


def format_progression_with_missing(progression, missing_index):
    progression[missing_index] = ".."
    return " ".join(map(str, progression))


def progression_game():
    current_number = random.randint(2, 100)
    length = random.randint(5, 10)
    step = random.randint(2, 10)
    missing_element = random.randint(2, length - 1)

    progression = create_progression(current_number, step, length)
    question = remove_el_from_progression(progression, missing_element)

    correct_answer = current_number + missing_element * step

    return (question, correct_answer)
