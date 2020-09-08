import prompt


def engin(rules, gen_question):
    print('\nWelcome to the Brain Games!')
    print(rules)
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {0}!\n'.format(name))

    count = 1
    while count <= 3:
        count += 1
        question, correct_answer = gen_question()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, correct_answer))
            print("Let's try again, {0}!".format(name))
            return
    print('Congratulations, {0}!'.format(name))
