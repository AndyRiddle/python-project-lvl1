import random

LOWER_LIMIT = 1
UPPER_LIMIT = 100

rules = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def gen_question_answer():
    question = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
