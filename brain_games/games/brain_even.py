#!/usr/bin/env python3
import prompt
import random
import sys
sys.path.append('/home/usman/python-project-49/brain_games')

from brain_games.cli import welcome_user

def even_game():
	corrects_in_row = 0
	number = 0
	answer = "no"
	correct_answer = "no"
	print('Answer "yes" if the number is even, otherwise answer "no".')

	while corrects_in_row < 3:
		number = random.randint(1, 100)
		if number % 2 == 0:
			correct_answer = "yes"
		else:
			correct_answer = "no"

		print(f'Question: {number}')
		answer = prompt.string('Your answer: ')

		if answer == correct_answer:
			corrects_in_row += 1
			print("Correct!")
		else:
			break

	if corrects_in_row == 3:
		print(f"Congratulations, {name}!")
	else:
		if correct_answer == "yes":
			print("'no' is wrong answer ;(. Correct answer was 'yes'.")
			print(f"Let's try again, {name}")
		else:
			print("'yes' is wrong answer ;(. Correct answer was 'no'.")
			print(f"Let's try again, {name}")


def main():
	global name
	name = welcome_user()	
	even_game()


if __name__ == "__main__":	
	main()
