import sys
import pygame

from settings import Settings
import game_functions as gf

def run_game():
    # Initialize and create game screen
    pygame.init()
    settings = Settings()                                                               # Set settings
    screen = pygame.display.set_mode( (settings.screen_width, settings.screen_height) ) # Initialize screen
    pygame.display.set_caption("Sudoku")
    unsolved_grid = gf.read_file(settings.solve_dir + "grid.txt")                       # Get unsolved grid
    solved_grid = gf.solve_grid(settings, settings.solve_dir + "solved_puzzle.txt")     # Solve grid, then get solved grid

    # Main loop for game
    while True:
        gf.check_events(settings, screen)
        if (settings.solved == True):
            gf.update_screen(settings, screen, solved_grid)
        else:
            gf.update_screen(settings, screen, unsolved_grid)

run_game()
