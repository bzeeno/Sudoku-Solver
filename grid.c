#include "sudoku.h"

int** create_grid() {
    int** grid;
    int i=0, j=0;
    char current_char;
    int array[9][9];

    // Open file with sudoku grid values
    FILE* f_ptr;
    f_ptr = fopen("grid.txt", "r");

    if (f_ptr == NULL) {
        printf("File not found. Exiting.");
        exit(1);
    }

    while ( (current_char = fgetc(f_ptr)) != EOF ) {
        if(current_char == ',' || current_char == ' ') { }
        else if (current_char == '\n') {
            ++i;
        }
        else {
            array[i][j] = (int)current_char - '0';

            if( j == 8) { j = 0; }
            else { ++j; }
        }
    }

    fclose(f_ptr);

    // Create 9 arrays
    grid = (int**)malloc(9*sizeof(int*));

    for (i = 0; i < 9; i++) {
        grid[i] = (int*)malloc(9*sizeof(int)); 
        for (j = 0; j < 9; j++) {
            grid[i][j] = array[i][j];
        }
    }

    return grid;

}

void print_grid(int** grid) {
    int i, j, row_count=0, col_count=0;

    for (i = 0; i < 9; i++) {
        printf("|");

        for (j = 0; j < 9; j++) {
            printf(" %d ", grid[i][j]);

            if(col_count==2) {
                printf("|");
                col_count = 0;
            } else {++col_count;}
        } 

        if(row_count == 2) {
            printf("\n-----------------------------\n");
            row_count = 0;
        }
        else {
            ++row_count;
            printf("\n");
        }
    }
}

void save_grid(int** grid) {
    int i,j;
    char current_char;

    FILE* f_ptr;
    f_ptr = fopen("solved_puzzle.txt", "w");

    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            // Convert grid number to char
            current_char = (char)grid[i][j] + '0';
            // write char to file
            fputc(current_char, f_ptr); 
            // No comma if final value
            if ( (i==8) && (j==8) ) {}
            // comma and space after every 3 values (width of one sudoku box)
            else if ( (j != 0) && ((j+1)%3 == 0) ) { 
                fputc(',', f_ptr);
                fputc(' ', f_ptr);
            }
            // comma after each value
            else {
                fputc(',', f_ptr);
            }
        }
        // New line at end of each row (unless last row)
        if (i == 8) { }
        else {
            fputc('\n', f_ptr);
        }
    }
    fclose(f_ptr);
}
