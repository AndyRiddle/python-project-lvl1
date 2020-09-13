import math
import random

LOWER_LIMIT_FIRST = 2
LOWER_LIMIT_SECOND = 1
UPPER_LIMIT = 100

rules_prime = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def number_prime(number):
    for divisor in range(LOWER_LIMIT_FIRST, math.ceil(math.sqrt(number))):
        if number % divisor == 0:
            return 'no'
        return 'yes'


def gen_question_prime():
    question = random.randint(LOWER_LIMIT_SECOND, UPPER_LIMIT)
    correct_answer = number_prime(question)
    return question, correct_answer
