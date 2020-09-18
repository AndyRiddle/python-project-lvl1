import math
import random

LOWER_LIMIT_FIRST = 2
LOWER_LIMIT_SECOND = 1
UPPER_LIMIT = 100

rules_prime = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def define_number_prime(number):
    for divisor in range(LOWER_LIMIT_FIRST, math.ceil(math.sqrt(number) + 1)):
        if number % divisor == 0 and number != 2:
            return False
    return True


def gen_question_answer_prime():
    question = random.randint(LOWER_LIMIT_SECOND, UPPER_LIMIT)
    if define_number_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
