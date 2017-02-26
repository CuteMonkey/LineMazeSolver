from LMsolver import *

first_flag = True
while True:
    if first_flag:
        print('Welcome to use this stupid line maze solver!!')
        first_flag = False
    else:
        print()
    print('Please enter the action number which you want to perfome.')
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
        answer_path = dfs_solver(line_maze_map)
        if len(answer_path) == 0:
            print('This puzzle has no answer.')
            continue
        write_answer(file_name, answer_path)
        print('This puzzle solved!')
    elif N == 2:
        break
    else:
        print('Invalid action number!')