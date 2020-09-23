from brain_games import engine
from brain_games.games import prime


def main():
    engine.start_game(prime.RULE, prime.gen_question_answer)


if __name__ == '__main__':
    main()
