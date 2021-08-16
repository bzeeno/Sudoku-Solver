# Sudoku-Solver
Sudoku solver is written in C and GUI is written in Python

Table of Contents
=================

   * [Introduction](#introduction)
   * [Directory Structure](#directory-structure)
   * [How To Use](#how-to-use)

## Introduction
This project solves sudoku puzzles using backtracking. The algorithm is implemented in C, while the GUI is implemented in python using pygame. 

## Directory Structure
<pre>
├── requirements.txt
├── GUI
│   ├── game_functions.py
│   ├── gui.py
│   └── settings.py
└── Solver
    ├── grid.c
    ├── grid.txt
    ├── solve.c
    ├── solved_puzzle.txt
    ├── sudoku
    ├── sudoku.c
    └── sudoku.h
</pre>

## How To Use
- To run the solver: 
  - cd into the GUI directory
  - run: python gui.py.
  - press space bar to solve the puzzle
