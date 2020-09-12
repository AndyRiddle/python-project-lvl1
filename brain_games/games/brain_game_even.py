import random

rules_even = 'Answer "yes" if number even otherwise answer "no".'


def number_even(number):
    if int(number) % 2 == 0:
        return 'yes'
    return 'no'


def gen_question_even():
    question = str(random.randint(1, 100))
    correct_answer = number_even(question)
    return question, correct_answer
