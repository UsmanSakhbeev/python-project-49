
import prompt
import random
import sys
sys.path.append('/home/usman/python-project-49/brain_games')

from cli import welcome_user

name = "Dyadya Bob"


def calc_game():
    first_number = 0
    second_number = 0
    operation = 0
    corrects_in_row = 0
    correct_answer = 0
    answer = '0'
    print("What is result of the expresion?")

    while corrects_in_row < 3:
        first_number = random.randint(2, 100)
        second_number = random.randint(2, 100)
        operation = random.randint(1, 3)
        if operation == 1:
            correct_answer = first_number + second_number
            print(f"Question: {first_number} + {second_number}")
        elif operation == 2:
            correct_answer = first_number - second_number
            print(f"Question: {first_number} - {second_number}")
        else:
            correct_answer = first_number * second_number
            print(f"Question: {first_number} * {second_number}")
        answer = prompt.string("Your answer: ")
        if answer == str(correct_answer):
            print("Correct!")
            corrects_in_row += 1
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
    calc_game()


if __name__ == "__main__":
    main()
