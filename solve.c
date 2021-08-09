#include "sudoku.h"

// Find next empty slot in grid
Position find_empty(int** grid) {
    int i, j;
    Position pos;

    for (i = 0; i < 9; i++) {
        for (j = 0; j<9; j++) {
            if (grid[i][j] == 0) {
                pos.row = i;
                pos.col = j;
                return pos;
            }
        }
    }    
    // return -1 if no more empty slots (puzzle is solved)
    pos.row = -1;
    pos.col = -1;
    return pos;
}

bool valid(int** grid, Position* cell, int num) {
    int i, j;
    int box_x, box_y;

    /* ROW CHECK */
    // loop through each value in row, and see if any of the values are equal to the number we are testing (num) 
    for (j = 0; j < 9; j++) {
        if ( (grid[cell->row][j] == num) && (cell->col != j) ) {  
            return false;
        }
    } 

    /* COLUMN CHECK */
    // loop through each value in col, and see if any of the values are equal to the number we are testing (num) 
    for (i = 0; i < 9; i++) {
        if ( (grid[i][cell->col] == num) && (cell->row != i) ) {
            return false;
        }
    }

    /* BOX CHECK */
    // Check if num is in 3x3 box
    // get box position [(0,1,2), (0,1,2)]
    box_x = cell->col / 3; // divide by 3 since there are 3 boxes in x-axis
    box_y = cell->row / 3; // "                                    " y-axis

    /* (box_y * 3) gives index of 0th row of box
     * (box_y * 3 + 3) gives final index in box
     * box_x gives same values (0th and final) but for columns
     */
    for (i = (box_y * 3); i < (box_y * 3 + 3); i++) {
        for (j = (box_x * 3); j < (box_x * 3 + 3); j++) {
            if ( (grid[i][j] == num) && (cell->row != i) && (cell->col != j) ) {
                return false;
            }
        }
    }

    return true;

}

bool solve(int** grid) {
    int i;
    int row, col;
    Position empty_pos;
    Position* pos_ptr;

    empty_pos = find_empty(grid); // Get next empty position
    pos_ptr = &empty_pos;         // set pointer to empty position

    if ( (empty_pos.row == -1) || (empty_pos.col == -1) ) { // if puzzle solving is complete
        return true;
    }
    else {                                                  // else: set row and col to empty positions
        row = empty_pos.row;
        col = empty_pos.col;
    }

    for (i = 1; i <= 9; i++) {              // for values 1 - 9:
        if ( valid(grid, pos_ptr, i) ) {    // if current value is valid:
            grid[row][col] = i;             // set empty position to value

            if ( solve(grid) ) {            // recursively call solve with new value
                return true;
            }
            grid[row][col] = 0; // if solve returned false (i.e. the next empty cell does not have a solution): reset current cell, and attempt next number
        }  
    }
    // if no number worked for current cell: return false so the previous cell can be re-evaluated
    return false;
}
