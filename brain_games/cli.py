import prompt


def welcome_user():
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {0}!'.format(name))
