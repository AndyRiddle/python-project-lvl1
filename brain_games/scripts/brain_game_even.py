import random

rules_even = 'Answer "yes" if number even otherwise answer "no".'


def gen_question_even():
    number = str(random.randint(1, 100))
    if int(number) % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
