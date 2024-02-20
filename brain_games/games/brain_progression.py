import prompt
import random
import sys
sys.path.append('/home/usman/python-project-49/brain_games')

from cli import welcome_user

name = "Dyadya Bob"


def progression_game():
    current_number = 0
    length_of_progression = 0
    step_of_progression = 0
    corrects_in_row = 0
    missing_element = 0
    current_element = 0
    correct_answer = 0
    answer = 0

    print("Find the greatest common divisor of given numbers.")

    while corrects_in_row < 3:
        current_number = random.randint(2, 100)
        length_of_progression = random.randint(5, 10)
        step_of_progression = random.randint(2, 10)
        missing_element = random.randint(2, length_of_progression)
        current_element = 0

        print("What number is missing in the progression?")
        print("Question: ", end="")
        while current_element <= length_of_progression:
            if current_element == missing_element:
                print(" ..", end="")
                current_number += step_of_progression
                correct_answer = current_number
                current_element += 1
            else:
                print(" ", + current_number + step_of_progression, end="")
                current_number += step_of_progression
                current_element += 1

        print()
        answer = prompt.string("Your answer: ")
        if str(correct_answer) == answer:
            corrects_in_row += 1
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break

    if corrects_in_row == 3:
        print(f"Congratulations, {name}")
    else:
        print(f"Let's try again, {name}")


def main():
    global name
    name = welcome_user()
    progression_game()


if __name__ == "__main__":
    main()
