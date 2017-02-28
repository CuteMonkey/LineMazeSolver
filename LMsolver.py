from LMlib import *
import itertools as ITs

def build_map(map_name):
    map_f_path =  'LMquestion/' + map_name + '.txt'
    try:
        map_f = open(map_f_path)
    except OSError:
        print('Can not open map file ' + map_name + '!')
        return None
    
    map_size = map_f.readline()
    map_size = map_size.partition(' ')
    map_size = (int(map_size[0]), int(map_size[2]))
    lm_map = LMmap(map_size[0], map_size[1])
    for row_i in range(lm_map.n_row):
        a_row = map_f.readline()
        a_row = a_row.split(' ')
        for col_i in range(lm_map.n_col):
            n_wall = int(a_row[col_i])
            if n_wall % 2 == 1:
                lm_map.set_wall(row_i, col_i, 'U')
            n_wall //= 2
            if n_wall % 2 == 1:
                lm_map.set_wall(row_i, col_i, 'D')
            n_wall //= 2
            if n_wall % 2 == 1:
                lm_map.set_wall(row_i, col_i, 'L')
            n_wall //= 2
            if n_wall % 2 == 1:
                lm_map.set_wall(row_i, col_i, 'R')
                
    map_f.close()
    return lm_map
    
def dfs_solver(lm_map):
    lm_map.update_gates()
    #lm_map.update_path_parts()
    
    n_grid = lm_map.n_row * lm_map.n_col
    gate_pairs = ITs.combinations(lm_map.gates, 2)
    
    possible_gate_pairs = []
    #remove impossible gate pairs
    for gate_pair in gate_pairs:
        manhatton_dist = abs(gate_pair[0][0] - gate_pair[1][0]) + abs(gate_pair[0][1] - gate_pair[1][1])
        if n_grid % 2 == 0:
            if manhatton_dist % 2 == 1:
                possible_gate_pairs.append(gate_pair)
        else:
            if manhatton_dist % 2 == 0:
                possible_gate_pairs.append(gate_pair)
    
    for a_gate_pair in possible_gate_pairs:
        dfs_grid_stack = []
        #record rhe number of new branch when extending a grid
        dfs_n_branch = []
        cur_path = []
    
        dfs_grid_stack.append(a_gate_pair[0])
        lm_map.clean_all_passed()
        while len(dfs_grid_stack) > 0:
            a_grid = dfs_grid_stack.pop()
                
            lm_map.set_passed(a_grid[0], a_grid[1])
            cur_path.append(a_grid)
            
            if a_grid == a_gate_pair[1] and len(cur_path) == n_grid:
                return cur_path
            
            n_new_branch = 0 
            if a_grid[0] != 0 and not lm_map.has_wall(a_grid[0], a_grid[1], 'U') and not lm_map.has_passed(a_grid[0] - 1, a_grid[1]):
                dfs_grid_stack.append((a_grid[0] - 1, a_grid[1]))
                n_new_branch += 1
            if a_grid[0] != lm_map.n_row - 1 and not lm_map.has_wall(a_grid[0], a_grid[1], 'D') and not lm_map.has_passed(a_grid[0] + 1, a_grid[1]):
                dfs_grid_stack.append((a_grid[0] + 1, a_grid[1]))
                n_new_branch += 1
            if a_grid[1] != 0 and not lm_map.has_wall(a_grid[0], a_grid[1], 'L') and not lm_map.has_passed(a_grid[0], a_grid[1] - 1):
                dfs_grid_stack.append((a_grid[0], a_grid[1] - 1))
                n_new_branch += 1
            if a_grid[1] != lm_map.n_col - 1 and not lm_map.has_wall(a_grid[0], a_grid[1], 'R') and not lm_map.has_passed(a_grid[0], a_grid[1] + 1):
                dfs_grid_stack.append((a_grid[0], a_grid[1] + 1))
                n_new_branch += 1
            
            if n_new_branch == 0:
                while True:
                    a_grid = cur_path.pop()
                    lm_map.clean_passed(a_grid[0], a_grid[1])
                    if len(dfs_n_branch) == 0:
                        break
                    elif dfs_n_branch[-1] > 1:
                        dfs_n_branch[-1] -= 1
                        break
                    else:
                        dfs_n_branch.pop()
            else:
                dfs_n_branch.append(n_new_branch)
    else:
        return []
                
def write_answer(map_name, n_row, n_col, ans_path):
    ans_f_path = 'LManswer/' + map_name + '.txt'
    ans_f = open(ans_f_path, 'w')
    
    ans_map = []
    for i in range(n_row):
        a_row = []
        for j in range(n_col):
            a_row.append(0)
        ans_map.append(a_row)
        
    index = 0
    for cord in ans_path:
        index += 1
        ans_map[cord[0]][cord[1]] = index
        
    number_width = len(str(index))
    format_str = '%0' + str(number_width) + 'd '
    for i in range(n_row):
        for j in range(n_col):
            print(format_str % ans_map[i][j], file=ans_f, end='')
        print(file=ans_f)
        
    ans_f.close()