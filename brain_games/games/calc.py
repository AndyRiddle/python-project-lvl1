import operator
import random

LOWER_LIMIT = 1
UPPER_LIMIT = 100
ARITHMETIC_OPERATIONS = (
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
)

RULE = 'What is the result of the expression?'


def gen_arithmetic_sign_answer(operand1, operand2):
    arithmetic_sign, operation = random.choice(ARITHMETIC_OPERATIONS)
    answer = str(operation(operand1, operand2))
    return arithmetic_sign, answer


def gen_question_answer():
    number1 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    number2 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    arithmetic_action, correct_answer = gen_arithmetic_sign_answer(number1, number2)
    question = '{0} {1} {2}'.format(number1, arithmetic_action, number2)
    return question, correct_answer
