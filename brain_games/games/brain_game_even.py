import random

LOWER_LIMIT = 1
UPPER_LIMIT = 100

rules_even = 'Answer "yes" if number even otherwise answer "no".'


def number_even(number):
    if int(number) % 2 == 0:
        return 'yes'
    return 'no'


def gen_question_even():
    question = str(random.randint(LOWER_LIMIT, UPPER_LIMIT))
    correct_answer = number_even(question)
    return question, correct_answer
