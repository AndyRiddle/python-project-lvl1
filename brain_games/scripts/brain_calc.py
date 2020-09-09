from brain_games.games import brain_game_calc
from brain_games import engine_brain_games


def main():
    engine_brain_games.engine(brain_game_calc.rules_calc, brain_game_calc.gen_question_calc)


if __name__ == '__main__':
    main()
