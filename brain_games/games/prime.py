import math
import random

FIRST_DIVISOR = 2
LOWER_LIMIT = 1
UPPER_LIMIT = 100

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(FIRST_DIVISOR, math.ceil(math.sqrt(number) + 1)):
        if (number % divisor == 0 and number != 2):
            return False
    return True


def gen_question_answer():
    question = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
