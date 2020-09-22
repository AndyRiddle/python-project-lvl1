from brain_games import engine
from brain_games.games import even


def main():
    engine.start_game(even.rules, even.gen_question_answer)


if __name__ == '__main__':
    main()
