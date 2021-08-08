#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Position {
    int row, col;
} Position;

int** create_grid();
void print_grid(int** grid);
Position find_empty(int** grid);
bool valid(int** grid, Position* cell, int num);
bool solve(int** grid);
void save_grid(int** grid);
