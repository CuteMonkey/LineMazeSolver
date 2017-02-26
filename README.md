# Line Maze Puzzle Solver

## How to use
Execute *LMsolverUI* python module, and perform according to UI.
Put maze map file in *LMquestion* directory, this solver can only accept .txt file.

Enter the file name of map file without format name.
For example, you want to let solver solve a puzzle whose map file is LMquestion/easy1_1.txt.
Then you only need to enter 'easy1_1'.

The answer file will be generated in *LManswer* directory, and its file name is same as map file's.

## Format of map file
The first contains 2 numbers - the numbers of rows and columns.
The following lines contain the wall status of each grid.

The wall status is a number, its a sum of walls at 4 directions.
*   Up: 1
*   Down: 2
*   Left: 4
*   Right: 8

The following is the map file of level 1 of Easy Episode 1:

    2 2
    06 09
    05 10

Those leading zeroes are only for read easily, not necessary.

## Format of answer file
A sequence of coordinates of right path.
The most up-right grid is (0, 0).