import random

LOWER_LIMIT = 1
UPPER_LIMIT_ELEMENT_PROGRESSION = 50
UPPER_LIMIT_STEP = 5
PROGRESSION_LENGTH = 10
RULE = 'What number is missing in the progression?'


def gen_progression():
    first_element_progression = random.randint(LOWER_LIMIT, UPPER_LIMIT_ELEMENT_PROGRESSION)
    step_progression = random.randint(LOWER_LIMIT, UPPER_LIMIT_STEP)
    progression = []
    for counter in range(PROGRESSION_LENGTH):
        progression.append(str(first_element_progression + step_progression * counter))
    return progression


def gen_question_answer():
    progression = gen_progression()
    correct_answer = random.choice(progression)
    index = progression.index(correct_answer)
    progression[index] = '..'
    string_progression = ' '.join(progression)
    question = '{0}'.format(string_progression)
    return question, correct_answer
