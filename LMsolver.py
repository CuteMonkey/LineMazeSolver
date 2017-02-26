from LMlib import *

def build_map(map_name):
    map_f_path =  'LMquestion/' + map_name + '.txt'
    try:
        map_f = open(map_f_path)
    except OSError:
        print('Can not open map file ' + map_name + '.')
        return
    
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