import random

rules_gcd = 'Find the greatest common divisor of given numbers.'


def gen_question_gcd():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = '{0} {1}'.format(number1, number2)
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    correct_answer = str(number1 + number2)
    return question, correct_answer
