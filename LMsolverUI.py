from LMsolver import *
import time

first_flag = True
while True:
    if first_flag:
        print('Welcome to use this simple line maze solver!!')
        first_flag = False
    else:
        print()
    print('Please enter the action number which you want to perform.')
    print('(1) Use solver')
    print('(2) Exit from solver')
    action_number = input('Action number: ')
    
    try:
        N = int(action_number)
    except ValueError:
        print('Not a number!')
        continue
    if N == 1:
        print('Please enter the file name of line maze map.')
        file_name = input('Map file name: ')
        line_maze_map = build_map(file_name)
        if line_maze_map == None:
            continue
            
        start_clk = time.clock()
        answer_path = dfs_solver(line_maze_map)
        end_clk = time.clock()
        if len(answer_path) == 0:
            print('This puzzle has no answer.')
            continue
        else:
            print('It took', '%f' % (end_clk - start_clk), 'seconds to solve this puzzle.')
            
        write_answer(file_name, line_maze_map.n_row, line_maze_map.n_col, answer_path)
        print('Answer file generated!')
    elif N == 2:
        break
    else:
        print('Invalid action number!')