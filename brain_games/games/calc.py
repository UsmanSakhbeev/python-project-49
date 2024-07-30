import random
import operator


game_rule = "What is the result of the expression?"


def get_operator_func(op):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    return operators[op]


def calc_game():
    first_number = random.randint(2, 100)
    second_number = random.randint(2, 100)
    operation = random.choice(['+', '-', '*'])
    operator_func = get_operator_func(operation)
    correct_answer = operator_func(first_number, second_number)
    question = f"{first_number} {operation} {second_number}"
    return (question, correct_answer)
