import math
import random

LOWER_LIMIT = 1
UPPER_LIMIT = 100

rules_gcd = 'Find the greatest common divisor of given numbers.'


def gen_question_gcd():
    number1 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    number2 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    question = '{0} {1}'.format(number1, number2)
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer
