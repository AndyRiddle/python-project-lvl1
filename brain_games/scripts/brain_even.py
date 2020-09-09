from brain_games.games import brain_game_even
from brain_games import engine_brain_games


def main():
    engine_brain_games.engine(brain_game_even.rules_even, brain_game_even.gen_question_even)


if __name__ == '__main__':
    main()
