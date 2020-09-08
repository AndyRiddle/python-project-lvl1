from brain_games.scripts import brain_game_calc, engin_brain_games


def main():
    engin_brain_games.engin(brain_game_calc.rules_calc, brain_game_calc.gen_question_calc)


if __name__ == '__main__':
    main()
