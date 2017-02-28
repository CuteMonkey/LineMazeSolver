class LMgrid:
    def __init__(self):
        self._Uwall = False
        self._Dwall = False
        self._Lwall = False
        self._Rwall = False
        self._n_wall = 0
        
        self.passed = False
        
        self.part_mid = False
        self.part_fend = False
        self.part_rend = False
        
    def set_wall(self, dir):
        if dir == 'U':
            self._Uwall = True
        elif dir == 'D':
            self._Dwall = True
        elif dir == 'L':
            self._Lwall = True
        elif dir == 'R':
            self._Rwall = True
        self._n_wall += 1
            
    def clean_wall(self, dir):
        if dir == 'U':
            self._Uwall = False
        elif dir == 'D':
            self._Dwall = False
        elif dir == 'L':
            self._Lwall = False
        elif dir == 'R':
            self._Rwall = False
        self._n_wall -= 1
            
    def has_wall(self, dir):
        if dir == 'U':
            return self._Uwall
        elif dir == 'D':
            return self._Dwall
        elif dir == 'L':
            return self._Lwall
        elif dir == 'R':
            return self._Rwall
            
    def count_wall(self):
        return self._n_wall
            
class LMmap:
    def __init__(self, n_row, n_col):
        self.n_row = n_row
        self.n_col = n_col
        
        self._map = []
        for i in range(self.n_row):
            a_row = []
            for j in range(self.n_col):
                a_row.append(LMgrid())
            self._map.append(a_row)
        
        self.gates = []
        #record the parts of answer path that can be identified directly
        self.path_parts = []
            
    def set_wall(self, row_i, col_i, dir):
        self._map[row_i][col_i].set_wall(dir)
        
    def clean_wall(self, row_i, col_i, dir):
        self._map[row_i][col_i].clean_wall(dir)
        
    def has_wall(self, row_i, col_i, dir):
        return self._map[row_i][col_i].has_wall(dir)
        
    def count_wall(self, row_i, col_i):
        return self._map[row_i][col_i].count_wall()
        
    def update_gates(self):
        self.gates.clear()
        for col_i in range(self.n_col):
            if not self.has_wall(0, col_i, 'U'):
                self.gates.append((0, col_i))
            if not self.has_wall(self.n_row - 1, col_i, 'D'):
                self.gates.append((self.n_row - 1, col_i))
        for row_i in range(self.n_row):
            if not self.has_wall(row_i, 0, 'L'):
                self.gates.append((row_i, 0))
            if not self.has_wall(row_i, self.n_col - 1, 'R'):
                self.gates.append((row_i, self.n_col - 1))
                
    def update_path_parts(self):
        self.path_parts.clear()
        #find out all basic patterns
        for i in range(self.n_row):
            for j in range(self.n_col):
                if self.count_wall(i, j) == 2:
                    #I-shaped patterns
                    if self.has_wall(i, j, 'U') and self.has_wall(i, j, 'D'):
                        if j == 0:
                            self.path_parts.append([(i, j), (i, j + 1)])
                        elif j == self.n_col - 1:
                            self.path_parts.append([(i, j - 1), (i, j)])
                        else:
                            self.path_parts.append([(i, j - 1), (i, j), (i, j + 1)])
                    elif self.has_wall(i, j, 'L') and self.has_wall(i, j, 'R'):
                        if i == 0:
                            self.path_parts.append([(i, j), (i + 1, j)])
                        elif i == self.n_row - 1:
                            self.path_parts.append([(i - 1, j), (i, j)])
                        else:
                            self.path_parts.append([(i - 1, j), (i, j), (i + 1, j)])
                    #L-shaped patterns
                    elif self.has_wall(i, j, 'U') and self.has_wall(i, j, 'L'):
                        if j == self.n_col - 1:
                            self.path_parts.append([(i, j), (i + 1, j)])
                        elif i == self.n_row - 1:
                            self.path_parts.append([(i, j), (i, j + 1)])
                        else:
                            self.path_parts.append([(i + 1, j), (i, j), (i, j + 1)])
                    elif self.has_wall(i, j, 'U') and self.has_wall(i, j, 'R'):
                        if j == 0:
                            self.path_parts.append([(i, j), (i + 1, j)])
                        elif i == self.n_row - 1:
                            self.path_parts.append([(i, j - 1), (i, j)])
                        else:
                            self.path_parts.append([(i, j - 1), (i, j), (i + 1, j)])
                    elif self.has_wall(i, j, 'D') and self.has_wall(i, j, 'L'):
                        if i == 0:
                            self.path_parts.append([(i, j), (i, j + 1)])
                        elif j == self.n_col - 1:
                            self.path_parts.append([(i - 1, j), (i, j)])
                        else:
                            self.path_parts.append([(i - 1, j), (i, j), (i, j + 1)])
                    elif self.has_wall(i, j, 'D') and self.has_wall(i, j, 'R'):
                        if i == 0:
                            self.path_parts.append([(i, j - 1), (i, j)])
                        elif j == 0:
                            self.path_parts.append([(i - 1, j), (i, j)])
                        else:
                            self.path_parts.append([(i, j - 1), (i, j), (i - 1, j)])
        
        while True:
            n_part = len(self.path_parts)
            if n_part == 1:
                break
            
            new_path_parts = []
            old_path_parts = list(self.path_parts)
            part_choosed = [False] * n_part
            for i in range(n_part):
                if not part_choosed[i]:
                    for j in range(i + 1, n_part):
                        if not part_choosed[j]:
                            if self._is_part_same(self.path_parts[i], self.path_parts[j]):
                                new_path_parts.append(self._combine_parts(self.path_parts[i], self.path_parts[j]))
                                part_choosed[i] = True
                                part_choosed[j] = True
                                old_path_parts.remove(self.path_parts[i])
                                old_path_parts.remove(self.path_parts[j])
                                break
            if len(new_path_parts) == 0:
                break
            else:
                self.path_parts = new_path_parts + old_path_parts
                
        #update in_part flag and part_flag of all grids
        for i in range(self.n_row):
            for j in range(self.n_col):
                self._map[i][j].part_mid = False
                self._map[i][j].part_fend = False
                self._map[i][j].part_rend = False
        for a_part in self.path_parts:
            for i in range(1, len(a_part) - 1):
                self._map[a_part[i][0]][a_part[i][1]].part_mid = True
            self._map[a_part[0][0]][a_part[0][1]].part_fend = True
            self._map[a_part[-1][0]][a_part[-1][1]].part_rend = True
                
    def is_part_mid(self, row_i, col_i):
        return self._map[row_i][col_i].part_mid
        
    def is_part_end(self, row_i, col_i):
        if self._map[row_i][col_i].part_fend:
            return (True, 'f')
        elif self._map[row_i][col_i].part_rend:
            return (True, 'r')
        else:
            return (False, None)
            
    #get the path part from a grid included in it
    def get_part(self, a_grid):
        for part in self.path_parts:
            if a_grid in part:
                return part
        return None
                
    def _is_part_same(self, part_a, part_b):
        for grid_a in part_a:
            for grid_b in part_b:
                if grid_a == grid_b:
                    return True
        return False
                
    def _combine_parts(self, part_a, part_b):
        a_start, a_end, b_start, b_end = -1, -1, -1, -1
        len_a, len_b = len(part_a), len(part_b)
        same_flag = False
        for i in range(len_a):
            if same_flag:
                if part_a[i] in part_b:
                    a_end = i
                else:
                    break
            else:
                if part_a[i] in part_b:
                    a_start, a_end = i, i
                    same_flag = True
                    
        same_flag = False
        for i in range(len_b):
            if same_flag:
                if part_b[i] in part_a:
                    b_end = i
                else:
                    break
            else:
                if part_b[i] in part_a:
                    b_start, b_end = i, i
                    same_flag = True
        
        #for debuging
        #print(a_start, a_end, b_start, b_end)
        
        #case that part_a contains part_b
        if b_end - b_start == len_b - 1:
            return part_a
        #case that part_b contains part_a
        elif a_end - a_start == len_a - 1:
            return part_b
        #partial overlapped case
        else:
            if part_a[a_start] == part_b[b_start] and part_a[a_end] == part_b[b_end]:
                if a_end == len_a - 1 and b_start == 0:
                    return part_a + part_b[b_end + 1:]
                elif a_start == 0 and b_end == len_b - 1:
                    return part_b + part_a[a_end + 1:]
            if part_a[a_start] == part_b[b_end] and part_a[a_end] == part_b[b_start]:
                if a_end == len_a - 1 and b_end == len_b - 1:
                    return part_a + part_b[:b_start][::-1]
                elif a_start == 0 and b_start == 0:
                    return  part_a[::-1] + part_b[b_end + 1:]
        #if it goes here, there is some errors about inputs
        print('Combine error!')
        return None
            
    def set_passed(self, row_i, col_i):
        self._map[row_i][col_i].passed = True
        
    def clean_passed(self, row_i, col_i):
        self._map[row_i][col_i].passed = False
        
    def clean_all_passed(self):
        for i in range(self.n_row):
            for j in range(self.n_col):
                self._map[i][j].passed = False
        
    def has_passed(self, row_i, col_i):
        return self._map[row_i][col_i].passed
        
    #debug function
    def show_map(self):
        print('map:')
        for row_i in range(self.n_row):
            for col_i in range(self.n_col):
                wall_status = ['X', 'X', 'X', 'X']
                if self.has_wall(row_i, col_i, 'U'):
                    wall_status[0] = 'U'
                if self.has_wall(row_i, col_i, 'D'):
                    wall_status[1] = 'D'
                if self.has_wall(row_i, col_i, 'L'):
                    wall_status[2] = 'L'
                if self.has_wall(row_i, col_i, 'R'):
                    wall_status[3] = 'R'
                for d in wall_status:
                    print(d, end='')
                if col_i != self.n_col - 1:
                    print(' ', end='')
            print()
            
    #debug function
    def show_gates(self):
        print('gates:')
        for gate in self.gates:
            print(gate)
            
    #debug function
    def show_path_parts(self):
        print('path parts:')
        for path_part in self.path_parts:
            print(path_part)