from brain_games import engine_brain_games
from brain_games.games import brain_game_progression


def main():
    engine_brain_games.engine(brain_game_progression.rules_progression, brain_game_progression.gen_question_progression)


if __name__ == '__main__':
    main()
