from brain_games import engine
from brain_games.games import progression


def main():
    engine.start_game(progression.RULE, progression.gen_question_answer)


if __name__ == '__main__':
    main()
