import sys
import subprocess
import os
import pygame

def check_events(settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # solve puzzle and show in screen
            if event.key == pygame.K_SPACE:
                settings.solved = True

def draw_lines(settings, screen, vertical):
    """ 
    Draw either vertical or horizontal lines
    cell_length and border_length refer to either width or height (depending on whether drawing horizontal or vertical lines 
    """
    if (vertical):
        cell_length = settings.cell_width
        border_length = settings.border_width
        border_endpoint = settings.border_height
    else:
        cell_length = settings.cell_height
        border_length = settings.border_height
        border_endpoint = settings.border_width

    i = 1
    while (i * cell_length) < border_length:
        line_width = 1 if (i % 3) > 0 else 3                                                              # if iterator divisible by 3, then make line wider

        if (vertical):
            point1 = (i * cell_length + settings.border_margin, settings.border_margin)                   # x = (width of cell + margin) * number of cell ||| y = margin (top border)
            point2 = (i * cell_length + settings.border_margin, border_endpoint + settings.border_margin) # x = same as point1                            ||| y = border height + margin (bottom border)
        else:
            point1 = (settings.border_margin, i * cell_length + settings.border_margin)                   # x = margin (left border)                 ||| y = (height of cell + margin) * number of cell
            point2 = (settings.border_margin + border_endpoint, i * cell_length + settings.border_margin) # x = border width + margin (right border) ||| y = same as point1

        # Draw lines
        pygame.draw.line( screen, settings.line_colors, pygame.Vector2(point1[0], point1[1]), pygame.Vector2(point2[0], point2[1]), line_width )
        # Iterate i
        i+=1

def read_file(filename):
    i = 0
    j = 0
    array = [[0] * 9 for i in range(9)]

    if not os.path.isfile(filename):
        print("File does not exist")
    else:
        file = open(filename, 'r')
        while True:
            current_char = file.read(1) # read 1 character at a time
            if not current_char:
                break
            elif ( (current_char == ',') or (current_char == ' ') ):
                continue
            elif ( (current_char == '\n') ):
                i+=1
                j = 0
            else:
                array[i][j] = int(current_char)
                j+=1
        file.close()
        return array 

def solve_grid(settings, filename):
    # compile c code
    result = subprocess.run(settings.c_compile)

    # run executable from c code
    current_dir = os.getcwd()                   # get current directory
    os.chdir(settings.solve_dir)                # change directory to where the solver executable is stored
    subprocess.run("./sudoku")                  # run executable
    os.chdir(current_dir)                       # change back to current directory

    # get solved puzzle
    solved_grid = read_file(filename)
    return solved_grid

def draw_numbers(settings, screen, grid):
    row = 0

    for row in range(9):
        for col in range (9):
            out = grid[row][col]
            if (out == 0): continue
            else:
                number = settings.font.render(str(out), True, settings.font_color)
                screen.blit(number, pygame.Vector2( (col * settings.cell_width) + 42, (row * settings.cell_height) + 35 ))

def draw_background(settings, screen):
    # Fill background
    screen.fill(settings.bg_color)
    # Draw border
    pygame.draw.rect( screen, settings.border_color, pygame.Rect(settings.border_margin, settings.border_margin, settings.border_width, settings.border_height), settings.border_line_width )


def update_screen(settings, screen, grid):
    # Redraw screen every iteration
    draw_background(settings, screen)
    # Draw vertical lines
    draw_lines(settings, screen, 1)
    # Draw horizontal lines
    draw_lines(settings, screen, 0)
    # Draw numbers
    draw_numbers(settings, screen, grid)

    # Display most recently drawn screen
    pygame.display.flip()

