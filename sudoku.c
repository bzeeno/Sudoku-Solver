#include "sudoku.h"

int main(int argc, char* argv[]) {
    int** grid;
    grid = create_grid(); 

    print_grid(grid);

    printf("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n");

    solve(grid);
    print_grid(grid);
    save_grid(grid);

    return 0;
}
