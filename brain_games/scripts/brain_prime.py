from brain_games import engine_brain_games
from brain_games.games import brain_game_prime


def main():
    engine_brain_games.engine(brain_game_prime.rules_prime, brain_game_prime.gen_question_prime)


if __name__ == '__main__':
    main()
