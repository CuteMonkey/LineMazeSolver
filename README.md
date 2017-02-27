# Line Maze Puzzle Solver

## Introduction
The solver is for a app game named "[Linemaze Puzzles](https://play.google.com/store/apps/details?id=com.gameindy.line&hl=zh_TW)".
Its algorithm is based on DFS.

## How to use
Execute *LMsolverUI* python module, and perform according to UI.
Put maze map file in *LMquestion* directory, this solver can only accept .txt file.

Enter the file name of map file without format name.
For example, you want to let solver solve a puzzle of which map file is LMquestion/easy1_1.txt.
Then you only need to enter "easy1_1".

The answer file will be generated in *LManswer* directory, and its file name is same as map file's.

## Format of map file
The first line contains 2 numbers - the numbers of rows and columns.
The following lines contain the wall status of each grid.

The wall status is a number that it is a sum of walls at 4 directions.
*   Up: 1
*   Down: 2
*   Left: 4
*   Right: 8

For example, there is a grid of which walls at up and left.
Then the wall status of this gird is 1+4=5.  

The following is the map file of level 1 of Easy Episode 1:

    2 2
    06 09
    05 10

Those leading zeroes are only for read easily, not necessary.

## Format of answer file
A answer path presented by a number matrix.
The start point is 1.