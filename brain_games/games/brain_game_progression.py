import random

rules_progression = 'What number is missing in the progression?'


def gen_progression():
    element = random.randint(1, 50)  # noqa: WPS432
    step = random.randint(1, 5)
    list_progression = [str(element)]
    for _ in range(9):  # noqa: WPS122
        element += step
        list_progression.append(str(element))
    return list_progression


def gen_question_progression():
    progression = gen_progression()
    correct_answer = random.choice(progression)
    key = progression.index(correct_answer)
    progression[key] = '..'
    string_progression = ' '.join(progression)
    question = '{0}'.format(string_progression)
    return question, correct_answer
