import prompt


round_counts = 3


def play_game(get_question_answer, game_rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{game_rules}')

    for _ in range(round_counts):
        question, correct_answer = get_question_answer()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')

        if player_answer != str(correct_answer):
            print(f'"{player_answer}" is a wrong answer ;(', end='')
            print(f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return

        print("Congratulations!")
    print(f'Congratulations, {name}!')
