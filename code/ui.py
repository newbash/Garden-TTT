import pygame

from constants import *
circle = pygame.image.load('../Assets/X.svg')
square = pygame.image.load('../Assets/O.svg')


def draw_grid(screen):
    w, h = screen.get_size()
    # Vertical lines
    pygame.draw.line(screen, 'black',
                     (w // 3, 0), (w // 3, h), 2)
    pygame.draw.line(screen, 'black',
                     (2 * w // 3, 0), (2 * w // 3, h), 2)
    # Horizontal lines
    pygame.draw.line(screen, 'black',
                     (0, h // 3), (w, h // 3), 2)
    pygame.draw.line(screen, 'black',
                     (0, 2 * h // 3), (w, 2 * h // 3), 2)


def draw_players(screen, grid):
    for row_idx in range(3):
        for col_idx in range(3):
            center_x = col_idx * cell_w + (cell_w // 2)
            center_y = row_idx * cell_h + (cell_h // 2)

            if grid[row_idx][col_idx] == 1:
                circle_rect = circle.get_rect(center=(center_x, center_y))
                screen.blit(circle, circle_rect)

            elif grid[row_idx][col_idx] == 2:
                square_rect = square.get_rect(center=(center_x, center_y))
                screen.blit(square, square_rect)
