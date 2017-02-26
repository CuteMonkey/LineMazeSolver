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
    lm_map.update_gates()
    return lm_map
    
def dfs_solver(lm_map):
    gate_pairs = ITs.combinations(lm_map.gates, 2)
    
    for a_gate_pair in gate_pairs:
        dfs_grid_stack = []
        cur_path = []
    
        dfs_grid_stack.append(a_gate_pair[0])
        lm_map.clean_all_passed()
        while len(dfs_grid_stack) > 0:
            a_grid = dfs_grid_stack.pop()
            lm_map.set_passed(a_grid[0], a_grid[1])
            cur_path.append(a_grid)
            
            if a_grid == a_gate_pair[1] and len(cur_path) == lm_map.n_row * lm_map.n_col:
                return cur_path
            
            has_possible_step = False
            if a_grid[0] != 0 and not lm_map.has_wall(a_grid[0], a_grid[1], 'U') and not lm_map.has_passed(a_grid[0] - 1, a_grid[1]):
                dfs_grid_stack.append((a_grid[0] - 1, a_grid[1]))
                if not has_possible_step:
                    has_possible_step = True
            if a_grid[0] != lm_map.n_row - 1 and not lm_map.has_wall(a_grid[0], a_grid[1], 'D') and not lm_map.has_passed(a_grid[0] + 1, a_grid[1]):
                dfs_grid_stack.append((a_grid[0] + 1, a_grid[1]))
                if not has_possible_step:
                    has_possible_step = True
            if a_grid[1] != 0 and not lm_map.has_wall(a_grid[0], a_grid[1], 'L') and not lm_map.has_passed(a_grid[0], a_grid[1] - 1):
                dfs_grid_stack.append((a_grid[0], a_grid[1] - 1))
                if not has_possible_step:
                    has_possible_step = True
            if a_grid[1] != lm_map.n_col - 1 and not lm_map.has_wall(a_grid[0], a_grid[1], 'R') and not lm_map.has_passed(a_grid[0], a_grid[1] + 1):
                dfs_grid_stack.append((a_grid[0], a_grid[1] + 1))
                if not has_possible_step:
                    has_possible_step = True
            
            if not has_possible_step:
                a_grid = cur_path.pop()
                lm_map.clean_passed(a_grid[0], a_grid[1])
                
def write_answer(map_name, right_path):
    ans_f_path = 'LManswer/' + map_name + '.txt'
    ans_f = open(ans_f_path, 'w')
    for grid in right_path:
        print(grid, file=ans_f)
    ans_f.close()