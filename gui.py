import sys
import pygame

from settings import Settings
import game_functions as gf

def run_game():
    # Initialize and create game screen
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode( (settings.screen_width, settings.screen_height) )
    pygame.display.set_caption("Sudoku")
    unsolved_grid = gf.read_file("grid.txt")
    solved_grid = gf.solve_grid(settings, "solved_puzzle.txt")

    # Main loop for game
    while True:
        gf.check_events(settings, screen)
        if (settings.solved == True):
            gf.update_screen(settings, screen, solved_grid)
        else:
            gf.update_screen(settings, screen, unsolved_grid)

run_game()
