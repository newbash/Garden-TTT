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


def menu_button_handler(event, pvp_button, solo_button):

    if pvp_button.is_clicked(event):

        pvp_button.alpha = 0
        solo_button.alpha = 0

        # Returns: solo_mode, grid, turn, move_count, game_over
        return False, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 0, False

    elif solo_button.is_clicked(event):

        solo_button.alpha = 0
        pvp_button.alpha = 0

        return True, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 0, False

    # Returns None if no button was clicked
    return None


                menu_button.draw(screen)
                pvp_button.draw(screen)

                if menu_button.is_clicked(event):
                    menu_button.alpha = 0
                    pvp_button.alpha = 0

                    menu_scene(screen)
                    running = False
                    break

                elif pvp_button.is_clicked(event):
                    menu_button.alpha = 0
                    pvp_button.alpha = 0

                    # pvp_scene(screen)

                    # Resets game
                    grid = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]
                    turn = 1
                    move_count = 0
                    game_over = False