"""
Import the module cli.

Welcomes to the Brain Games.

Performs the welcome_use function.
"""
from brain_games import cli


def greeting():
    """Welcome to the Brain Games."""
    print('Walcome to the Brain Games!')


def main():
    """Perform the welcome functions."""
    greeting()
    cli.welcome_user()


if __name__ == '__main__':
    main()
