import pygame

from constants import *

from button import Button

pygame.init()
clock = pygame.time.Clock()
bg_image = pygame.image.load('../Assets/ticky.png')
bg_image = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Variables

solo_button = Button(WINDOW_WIDTH // 2 - 100,
                     WINDOW_HEIGHT // 2 - 25, 200, 50,
                     'Solo Mode', 'orange1', 'orange3')

pvp_button = Button(WINDOW_WIDTH // 2 - 100,
                    WINDOW_HEIGHT // 2 + (WINDOW_HEIGHT // 4) - 25, 200, 50,
                    'PvP Mode', 'orange1', 'orange3')

menu_button = Button(WINDOW_WIDTH // 2 - 100,
                     WINDOW_HEIGHT // 2 - 25, 200, 50,
                     'Menu', 'orange1', 'orange3')


# Game State
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
turn = 1  # random.randint(1, 2)
move_count = 0
game_over = False
solo_mode = False


def pvp_scene(screen):
    from logic import game_step_handler

    from ui import draw_players

    global grid, turn, move_count, game_over, solo_mode
    pygame.display.set_caption('TickyTacky - PvP Mode')

    running = True
    next_scene = None

    while running:

        for event in pygame.event.get():  # Event loop
            if event.type == pygame.QUIT:  # Breaks loop if user exits
                next_scene = 'quit'
                running = False
                break

            # Takes user input and translates it into grid update
            if not game_over:
                turn, move_count, game_over = game_step_handler(event, grid, turn,
                                                                move_count, cell_w,
                                                                cell_h)

            else:
                pvp_button.draw(screen)
                menu_button.draw(screen)

                if menu_button.is_clicked(event):
                    menu_button.alpha = 0
                    pvp_button.alpha = 0
                    next_scene = 'menu'
                    running = False
                    break

                elif pvp_button.is_clicked(event):
                    pvp_button.alpha = 0
                    menu_button.alpha = 0

                    # Resets game
                    grid = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]
                    turn = 1
                    move_count = 0
                    game_over = False

        screen.blit(bg_image, (0, 0))  # Inserts Background
        draw_players(screen, grid)  # Draws Xs and Os on grid

        if game_over:
            pvp_button.draw(screen)
            menu_button.draw(screen)

        pygame.display.update()  # Pushes changes to current window
        clock.tick(60)

    # Save game copy for future reference
    print(grid)
    return next_scene


def solo_scene(screen):  # later on, maybe add difficulty selection here
    pygame.display.set_caption('TickyTacky - Solo Mode')
    screen.fill('purple1')


def menu_scene(screen):
    from logic import menu_button_handler
    pygame.display.set_caption('TickyTacky')

    running = True
    next_scene = None
    next_payload = None

    while running:

        for event in pygame.event.get():  # Event loop
            if event.type == pygame.QUIT:  # Breaks loop if user exits
                next_scene = 'quit'
                running = False
                break

            result = menu_button_handler(
                event, screen, pvp_button, solo_button)
            if result == 'pvp':
                next_scene = result
                running = False
                break
            elif result == 'solo':
                next_scene = result
                running = False
                break

        # Visual components
        screen.blit(bg_image, (0, 0))  # Inserts Background
        pvp_button.draw(screen)
        solo_button.draw(screen)

        pygame.display.update()  # Pushes changes to current window
        clock.tick(60)

    return next_scene, next_payload
