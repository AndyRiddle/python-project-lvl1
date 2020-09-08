import random

arithmetic_operations = ['+', '-', '*']

rules_calc = 'What is the result of the expression?'


def gen_question_calc():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(arithmetic_operations)
    question = '{0} {1} {2}'.format(number1, operation, number2)
    if operation == '+':
        correct_answer = str(number1 + number2)
    elif operation == '-':
        correct_answer = str(number1 - number2)
    elif operation == '*':
        correct_answer = str(number1 * number2)
    return question, correct_answer
