import prompt
import random
import sys
sys.path.append('/home/usman/python-project-49/brain_games')

from brain_games.cli import welcome_user

name = "Dyadya Bob"


def gcd_game():
    first_number = 0
    second_number = 0
    remainder = 1
    corrects_in_row = 0
    correct_answer = 0
    answer = '0'
    print("Find the greatest common divisor of given numbers.")

    while corrects_in_row < 3:
        first_number = random.randint(2, 100)
        second_number = random.randint(2, 100)
        print(f"Question: {first_number} {second_number}")

        if first_number < second_number:
            first_number, second_number = second_number, first_number

        while remainder != 0:
            remainder = first_number % second_number
            first_number = second_number
            second_number = remainder

        remainder = 1
        correct_answer = first_number        
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
    gcd_game()


if __name__ == "__main__":
    main()
