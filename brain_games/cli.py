import prompt

def welcome_user():
	print("Welcome to the Brain Games!")
	name = prompt.string("May i have your name? ")
	print(f"Hello, {name}!")
	return name


def main():
	welcome_user()


if __name__ == '__main__':
	main()
