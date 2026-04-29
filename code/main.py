# Importing required libs and modules
import pygame

import random

import sys

from constants import *

from logic import input_handler

from ui import draw_players

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
#! make git and github
# change screen size, and center the tictac
# make game conclusion visual
# make menu overlayed over game conclusion
# make visual turn indicator (now is Xs turn)

# Game State
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
turn = random.randint(1, 2)
move_count = 0
running = True
game_over = False

while running:

    for event in pygame.event.get():  # Event loop
        if event.type == pygame.QUIT:  # Breaks loop if user exits
            running = False

        # Takes user input and translates it into grid update
        if not game_over:
            turn, move_count = input_handler(
                event, grid, turn, move_count, cell_w, cell_h)

    # Visual components
    screen.blit(bg_image, (0, 0))  # Inserts Background
    draw_players(screen, grid)
    # * draw_grid(screen) # debug

    pygame.display.update()  # Pushes changes to current window
    clock.tick(60)

# Save game copy for future reference
game_history(grid)
print(grid)

pygame.quit()
sys.exit()
