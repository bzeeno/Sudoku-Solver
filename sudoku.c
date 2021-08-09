#include "sudoku.h"

int main(int argc, char* argv[]) {
    // Get unsolved grid
    int** grid;
    grid = create_grid(); 
    // Solve grid and save to file
    solve(grid);
    save_grid(grid);

    return 0;
}
