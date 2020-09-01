import random

import prompt


def welcome_user():
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name


def greeting():
    print('Walcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')


def game_even(user_name):
    count = 1
    while count <= 3:
        count += 1
        number = random.randint(1, 100)
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer != 'yes':
            correct_answer = 'yes'
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, correct_answer))
            return ("Let's try again, {0}!".format(user_name))
        elif number % 2 == 1 and answer != 'no':
            correct_answer = 'no'
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, correct_answer))
            return ("Let's try again, {0}!".format(user_name))
        else:
            print('Correct!')
    return 'Congratulations, {0}!'.format(user_name)


def main():
    greeting()
    user_name = welcome_user()
    print(game_even(user_name))


if __name__ == '__main__':
    main()
