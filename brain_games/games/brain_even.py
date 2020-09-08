from brain_games.scripts import brain_game_even, engin_brain_games


def main():
    engin_brain_games.engin(brain_game_even.rules_even, brain_game_even.gen_question_even)


if __name__ == '__main__':
    main()
