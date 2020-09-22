import random

LOWER_LIMIT = 1
UPPER_LIMIT = 100

rules = 'Find the greatest common divisor of given numbers.'


def find_gcd(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    return first_number + second_number


def gen_question_answer():
    number1 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    number2 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    question = '{0} {1}'.format(number1, number2)
    correct_answer = str(find_gcd(number1, number2))
    return question, correct_answer
