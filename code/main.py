# Importing required libs and modules
import pygame

import random

import sys

from constants import *

from logic import button_handler, game_step_handler, best_move, check_status

from ui import draw_players

from button import Button

from debug import game_history

# Boilerplate code and Initiation
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('TickyTacky')
bg_image = pygame.image.load('../Assets/ticky2.svg')
bg_image = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

#! Temp notes
# * also make todolist, maybe using bookmarks exten
# make whole game UI in affinity
# change screen size, and center the tictac
# make game conclusion visual
# make menu overlayed over game conclusion
# make visual turn indicator (now is Xs turn)

# Variables

solo_button = Button(WINDOW_WIDTH // 2 - 100,
                     WINDOW_HEIGHT // 2 - 25, 200, 50,
                     "Solo Mode", 'orange1', 'orange3')

pvp_button = Button(WINDOW_WIDTH // 2 - 100,
                    WINDOW_HEIGHT // 2 + (WINDOW_HEIGHT // 4) - 25, 200, 50,
                    "PvP Mode", 'orange1', 'orange3')


# Game State
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
turn = 1  # random.randint(1, 2)
move_count = 0
running = True
game_over = False
solo_mode = False

running = True
while running:

    # Computer turn logic for solo mode
    if not game_over and solo_mode and turn == 2:
        move = best_move(grid)
        if move:
            row, col = move
            grid[row][col] = 2
            move_count += 1
            turn = 1
            if check_status(grid):
                game_over = True

    for event in pygame.event.get():  # Event loop
        if event.type == pygame.QUIT:  # Breaks loop if user exits
            running = False

        # Processes gameplay and check for win/tie conditions
        if not game_over:

            if turn == 1:
                turn, move_count, game_over = game_step_handler(event, grid, turn,
                                                                move_count, cell_w, cell_h)

            elif turn == 2 and not solo_mode:
                turn, move_count, game_over = game_step_handler(event, grid, turn,
                                                                move_count, cell_w, cell_h)

            if game_over:
                pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN])

        else:

            # Takes the result
            result = button_handler(event, pvp_button, solo_button)

            # Updates the state if a button was clicked
            if result is not None:
                solo_mode, grid, turn, move_count, game_over = result

    # Visual components
    screen.blit(bg_image, (0, 0))  # Inserts Background
    draw_players(screen, grid)  # Draws Xs and Os on grid

    if game_over:
        pvp_button.draw(screen)
        solo_button.draw(screen)

    pygame.display.update()  # Pushes changes to current window
    clock.tick(60)

# Save game copy for future reference

print(grid)

pygame.quit()
sys.exit()
