import random

LOWER_LIMIT = 1
UPPER_LIMIT_FIRST = 50
UPPER_LIMIT_SECOND = 5
LIST_LENGTH = 10

rules_progression = 'What number is missing in the progression?'


def gen_progression():
    element = random.randint(LOWER_LIMIT, UPPER_LIMIT_FIRST)
    step = random.randint(LOWER_LIMIT, UPPER_LIMIT_SECOND)
    list_progression = []
    for count in range(LIST_LENGTH):
        list_progression.append(str(element + step * count))
    return list_progression


def gen_question_answer_progression():
    progression = gen_progression()
    correct_answer = random.choice(progression)
    key = progression.index(correct_answer)
    progression[key] = '..'
    string_progression = ' '.join(progression)
    question = '{0}'.format(string_progression)
    return question, correct_answer
