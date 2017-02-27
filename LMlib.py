class LMgrid:
    def __init__(self):
        self._Uwall = False
        self._Dwall = False
        self._Lwall = False
        self._Rwall = False
        self._n_wall = 0
        self.passed = False
        
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
        self._map = []
        self.n_row = n_row
        self.n_col = n_col
        for i in range(n_row):
            a_row = []
            for j in range(n_col):
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
        self.gates = []
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
        for i in range(self.n_row):
            for j in range(self.n_col):
                if self.count_wall(i, j) == 2:
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
                            
        new_path_parts = []
        while True:
            pass
                
    def _combine_parts(part_a, part_b):
        pass
                
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