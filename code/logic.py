import pygame

import math

from constants import *

from scenes import menu_scene, pvp_scene  # , solo_scene

from debug import game_history


def shape_identifier(row, col, grid, turn, move_count):
    if grid[row][col] == 0:

        # Decides number put in grid
        grid[row][col] = turn

        # Increments the move counter value
        move_count += 1

    return move_count


def get_winner(grid):
    "returns 1 or 2 for the winning player, or 0 if no winner."
    # Rows
    for r in range(3):
        if grid[r][0] == grid[r][1] == grid[r][2] != 0:
            return grid[r][0]

    # Columns
    for c in range(3):
        if grid[0][c] == grid[1][c] == grid[2][c] != 0:
            return grid[0][c]

    # Diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]

    if grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return grid[0][2]

    return 0


def check_status(grid):
    winner = get_winner(grid)
    if winner:
        print(f"Player {winner} wins!")
        # pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN])
        game_history(grid)
        return winner

    # check for Tie
    for r in grid:
        if 0 in r:
            return None
    # pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN])
    print("Players tie!")
    game_history(grid)
    return 'Tie'


def mouse_input_handler(event: pygame.event.Event, grid, turn,
                        move_count, cell_w, cell_h):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos

        # Convert pixel position to grid coordinates
        col = mouse_x // cell_w
        row = mouse_y // cell_h

        # Saves previous move_count to check for changes
        prev_move_count = move_count  # * test

        # Updates the grid and move_count
        move_count = shape_identifier(
            row, col, grid, turn, move_count)

        # Sees if new move made, then activates a status check
        if move_count > prev_move_count:

            # * debug
            if turn == 1:  # * debug
                print(
                    f"X's turn, turn value: {turn}")
            elif turn == 2:
                print(
                    f"O's turn, turn value: {turn}")
            print(f"Move No.{move_count}")  # * debug

            # check_status(grid)
            turn = 2 if turn == 1 else 1

    return turn, move_count


def game_step_handler(event, grid, turn, move_count, cell_w, cell_h):

    prev_move_count = move_count
    turn, move_count = mouse_input_handler(event, grid, turn,
                                           move_count, cell_w, cell_h)

    if move_count > prev_move_count:
        if check_status(grid):
            return turn, move_count, True

    return turn, move_count, False


def minimax(grid, depth, alpha, beta, is_maximizing):
    winner = get_winner(grid)
    if winner == 2:
        return 10 - depth
    elif winner == 1:
        return depth - 10
    elif all(cell != 0 for row in grid for cell in row):
        return 0

    # Maximizing player (Computer)
    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if grid[row][col] == 0:
                    grid[row][col] = 2
                    eval = minimax(grid, depth +
                                   1, alpha, beta, False)
                    grid[row][col] = 0
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval

    # Minimizing player (Human)
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if grid[row][col] == 0:
                    grid[row][col] = 1
                    eval = minimax(grid, depth + 1, alpha, beta, True)
                    grid[row][col] = 0
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def best_move(grid):
    best_score = -math.inf
    move = None

    for row in range(3):
        for col in range(3):
            if grid[row][col] == 0:
                grid[row][col] = 2
                score = minimax(grid, 0, -math.inf, math.inf, False)
                grid[row][col] = 0

                if score > best_score:
                    best_score = score
                    move = (row, col)

    return move


def menu_button_handler(event, screen, pvp_button, solo_button):

    if pvp_button.is_clicked(event):

        pvp_button.alpha = 0
        solo_button.alpha = 0

        return 'pvp'

    elif solo_button.is_clicked(event):

        solo_button.alpha = 0
        pvp_button.alpha = 0

        # return True, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 0, False
        return 'solo'

    # Returns None if no button was clicked
    return None
