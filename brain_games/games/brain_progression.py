import random


game_rule = "What number is missing in the progression?"


def progression_game():
    current_number = random.randint(2, 100)
    length_of_progression = random.randint(5, 10)
    step_of_progression = random.randint(2, 10)
    missing_element = random.randint(2, length_of_progression)
    current_element = 0
    question = ""

    while current_element <= length_of_progression:
        if current_element == missing_element:
            question += ".. "
            current_number += step_of_progression
            correct_answer = current_number
            current_element += 1
        else:
            question += f"{current_number + step_of_progression} "
            current_number += step_of_progression
            current_element += 1

    return (question, correct_answer)
