from brain_games import engine
from brain_games.games import prime


def main():
    engine.start_game(prime.rules_prime, prime.gen_question_answer_prime)


if __name__ == '__main__':
    main()
