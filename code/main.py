# Importing required libs and modules
import pygame

import sys

from constants import *

from scenes import menu_scene, pvp_scene  # , solo_scene

#! Temp notes
# * also make todo list, maybe using bookmarks exten
# make whole game UI in affinity
# change screen size, and center the tictac in the screen or at least the stump
# make visual turn indicator (now is Xs turn)

# improve and add comments overall
# create solo mode with minimax algorithm and alpha beta pruning
# in menu, create visual for the game title in maybe the first 1/4 and center
#   of the screen
# make visual in the conclusion stating the player who won or if it was a tie
# add solo button to pvp conclusion screen and vise versa (maybe make it centered
# or maybe make it beside the pvp button, sharing the space in 3/4 of the screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('TickyTacky')

    current = 'menu'
    payload = None

    while True:
        if current == 'menu':
            next_scene, next_payload = menu_scene(screen)
            if next_scene is None:
                current = 'menu'
            elif next_scene == 'quit':
                break
            else:
                current = next_scene
                payload = next_payload

        elif current == 'pvp':
            next_scene = pvp_scene(screen)
            if next_scene is None:
                current = 'menu'
            elif next_scene == 'quit':
                break
            else:
                current = next_scene  # e.g., 'menu'
        else:
            # unknown state, return to menu
            current = 'menu'
    # cleanup and exit
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
