# Importing required libs and modules
import pygame

import random

import sys

from constants import *

from logic import game_step_handler

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
again_button = Button(WINDOW_WIDTH // 2 - 100,
                      WINDOW_HEIGHT // 2 + 50, 200, 50,
                      "Play Again", 'orange1', 'orange3')

# Game State
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
turn = 1  # random.randint(1, 2)
move_count = 0
running = True
game_over = False

while running:

    for event in pygame.event.get():  # Event loop
        if event.type == pygame.QUIT:  # Breaks loop if user exits
            running = False

        # Processes gameplay and check for win/tie conditions
        if not game_over:

            turn, move_count, game_over = game_step_handler(
                event, grid, turn, move_count, cell_w, cell_h)

            if game_over:
                pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN])

        if game_over:
            if again_button.is_clicked(event):
                # RESET EVERYTHING
                grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                turn = 1  # random.randint(1, 2)
                move_count = 0
                game_over = False
                again_button.alpha = 0

    # Visual components
    screen.blit(bg_image, (0, 0))  # Inserts Background
    draw_players(screen, grid)

    if game_over:
        again_button.draw(screen)

    # * draw_grid(screen) # debug

    pygame.display.update()  # Pushes changes to current window
    clock.tick(60)

# Save game copy for future reference

print(grid)

pygame.quit()
sys.exit()
