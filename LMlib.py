class LMgrid:
    def __init__(self):
        self._Uwall = False
        self._Dwall = False
        self._Lwall = False
        self._Rwall = False
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
            
    def clean_wall(self, dir):
        if dir == 'U':
            self._Uwall = False
        elif dir == 'D':
            self._Dwall = False
        elif dir == 'L':
            self._Lwall = False
        elif dir == 'R':
            self._Rwall = False
            
    def has_wall(self, dir):
        if dir == 'U':
            return self._Uwall
        elif dir == 'D':
            return self._Dwall
        elif dir == 'L':
            return self._Lwall
        elif dir == 'R':
            return self._Rwall
            
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
            
    def set_wall(self, row_i, col_i, dir):
        self._map[row_i][col_i].set_wall(dir)
        
    def clean_wall(self, row_i, col_i, dir):
        self._map[row_i][col_i].clean_wall(dir)
        
    def has_wall(self, row_i, col_i, dir):
        return self._map[row_i][col_i].has_wall(dir)
        
    def update_gates(self):
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
        for gate in self.gates:
            print(gate)