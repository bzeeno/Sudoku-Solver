import pygame

class Settings():
    """ Settings for sudoku game """

    def __init__(self):
        """ Initialize sudoku settings """

        self.solve_dir = "../Solver/"                                           # Directory with C code
        
        self.solved = False                                                 # Boolean to tell if puzzle is solved
        self.c_compile = ["gcc", "sudoku.c", "grid.c", "solve.c", "-o", "sudoku", self.solve_dir]

        # Screen settings
        self.screen_width = 800                                             # Screen Width
        self.screen_height = 800                                            # Screen Height
        self.bg_color = (255, 255, 255)                                     # Background color (white)

        # Border settings
        self.border_line_width = 3                                          # width of border lines
        self.border_color = (0, 0, 0)                                       # Color of border (black)
        self.border_margin = 15                                             # Left and Top margin of border
        self.border_width = self.screen_width - (2 * self.border_margin)    # Width of border
        self.border_height = self.screen_height - (2 * self.border_margin)  # Height of border

        # Line colors
        self.line_colors = (0, 0, 0)                                        # Color of interior lines (non-border lines)

        # Cell settings (a cell is where the numbers in the sudoku puzzle are located)
        self.cell_width = self.border_width / 9                             # Width of single cell
        self.cell_height = self.border_height / 9                           # Height of single cell

        self.font = pygame.font.SysFont(None, 80)
        self.font_color = (0, 0, 0)

