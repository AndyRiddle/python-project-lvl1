"""
Importing the library prompt.

Ask for a name and say 'Hello'.
"""
import prompt


def welcome_user():
    """
    Get the user name.

    Say 'Hello' to the user.
    """
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {0}!'.format(name))
