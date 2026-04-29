import pygame

from constants import *


def shape_identifier(row, col, grid, turn, move_count):
    if grid[row][col] == 0:

        # Decides number put in grid
        grid[row][col] = turn

        # Increments the move counter value
        move_count += 1

    return move_count


def get_winner(grid):
    "Returns 1 or 2 for the winning player, or 0 if no winner."
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
        pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN])
        return winner

    # check for Tie
    for r in grid:
        if 0 in r:
            return None
    pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN])
    print("Players tie!")
    return 'Tie'


def input_handler(event: pygame.event.Event, grid, turn, move_count, cell_w, cell_h):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos

        # Convert pixel position to grid coordinates
        col = mouse_x // cell_w
        row = mouse_y // cell_h

        # Saves previous move_count to check for changes
        prev_move_count = move_count  # * test

        # Updates the grid and move_count
        move_count = shape_identifier(row, col, grid, turn, move_count)

        # Sees if new move made, then activates a status check
        if move_count != prev_move_count:

            # * debug
            if turn == 1:  # * debug
                print(f"X's turn, turn value: {turn}")
            elif turn == 2:
                print(f"O's turn, turn value: {turn}")
            print(f"Move No.{move_count}")  # * debug

            check_status(grid)
            turn = 2 if turn == 1 else 1

    return turn, move_count
