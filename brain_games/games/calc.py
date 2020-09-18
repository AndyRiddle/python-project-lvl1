import operator
import random

LOWER_LIMIT = 1
UPPER_LIMIT = 100

arithmetic_operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}

rules_calc = 'What is the result of the expression?'


def gen_question_answer_calc():
    number1 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    number2 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    key = random.choice(list(arithmetic_operations.keys()))
    question = '{0} {1} {2}'.format(number1, key, number2)
    correct_answer = str(arithmetic_operations[key](number1, number2))
    return question, correct_answer
