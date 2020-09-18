import random

LOWER_LIMIT = 1
UPPER_LIMIT = 100

rules_even = 'Answer "yes" if number even otherwise answer "no".'


def define_number_even(number):
    if int(number) % 2 == 0:
        return True
    return False


def gen_question_answer_even():
    question = str(random.randint(LOWER_LIMIT, UPPER_LIMIT))
    if define_number_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
