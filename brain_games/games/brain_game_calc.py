import operator
import random

arithmetic_operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}

rules_calc = 'What is the result of the expression?'


def gen_question_calc():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    key = random.choice(list(arithmetic_operations.keys()))
    question = '{0} {1} {2}'.format(number1, key, number2)
    correct_answer = str(arithmetic_operations[key](number1, number2))
    return question, correct_answer
