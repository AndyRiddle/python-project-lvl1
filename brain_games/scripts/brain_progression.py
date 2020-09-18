from brain_games import engine
from brain_games.games import progression


def main():
    engine.start_game(progression.rules_progression, progression.gen_question_answer_progression)


if __name__ == '__main__':
    main()
