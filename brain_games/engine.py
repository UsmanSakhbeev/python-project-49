import prompt

def play_game(game_logic, game_rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{game_rules}')

    for _ in range(3):
        question, correct_answer = game_logic()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')

        if player_answer != str(correct_answer):
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Congratulations!")
    print(f'Congratulations, {name}!')