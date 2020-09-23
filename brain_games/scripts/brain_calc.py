from brain_games import engine
from brain_games.games import calc


def main():
    engine.start_game(calc.RULE, calc.gen_question_answer)


if __name__ == '__main__':
    main()
