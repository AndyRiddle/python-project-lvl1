from brain_games import engine_brain_games
from brain_games.games import brain_game_gcd


def main():
    engine_brain_games.engine(brain_game_gcd.rules_gcd, brain_game_gcd.gen_question_gcd)


if __name__ == '__main__':
    main()
