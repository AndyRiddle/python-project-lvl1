from brain_games import engine
from brain_games.games import gcd


def main():
    engine.start_game(gcd.rules, gcd.gen_question_answer)


if __name__ == '__main__':
    main()
