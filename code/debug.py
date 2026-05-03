from constants import *


def game_history(state):
    # Save the grid state cumulatively before exiting
    with open('../.venv/game_history.txt', 'a') as file:
        game_num = sum(1 for line in open(
            '../.venv/game_history.txt')) // 4 + 1
        file.write('~~~Game Result No.{}: ~~~\n'.format(game_num))
        for row in state['grid']:
            file.write('{}\n'.format(row))
