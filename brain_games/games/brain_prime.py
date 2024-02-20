import prompt
import random
import sys
sys.path.append('/home/usman/python-project-49/brain_games')

from cli import welcome_user

name = "Dyadya Bob"


def is_prime_game():
    number = 0
    corrects_in_row = 0
    correct_answer = "False"
    answer = '0'
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")

    while corrects_in_row < 3:
        number = random.randint(2, 200)
        print(f"Question: {number}")

        divider = 2
        while number % divider != 0:
            divider += 1
        if divider == number:
            correct_answer = "yes"
        else:
            correct_answer = "no"

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
    is_prime_game()


if __name__ == "__main__":
    main()
