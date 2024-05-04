import random


game_rule = "What number is missing in the progression?"


def create_progression(current_number, step_of_progression, length_of_progression):
    return [current_number + i*step_of_progression for i in range(length_of_progression)]


def remove_el_from_progression(list, missing_element):    
    string = ""
    for index, value in enumerate(list):
        if index != missing_element:
            string += str(value) + " "
        else:
            string += ".. "
    return string



def progression_game():
    current_number = random.randint(2, 100)
    length_of_progression = random.randint(5, 10)
    step_of_progression = random.randint(2, 10)
    missing_element = random.randint(2, length_of_progression)

    progression = create_progression(current_number, step_of_progression, length_of_progression)
    question = remove_el_from_progression(progression, missing_element)

    correct_answer = current_number + missing_element * step_of_progression

    return (question, correct_answer)
