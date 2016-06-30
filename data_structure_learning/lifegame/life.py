class Life(object):
    def __init__(self, num_of_row=10, num_of_column=10):
        self.grid = []
        self.next_grid = []
        self.num_live_neighbor = []
        self.next_num_live_neighbor = []
        for r in range(num_of_row):
            self.grid.append([0]*num_of_column)
            self.next_grid.append([0]*num_of_column)
            self.num_live_neighbor.append([0]*num_of_column)
            self.next_num_live_neighbor.append([0]*num_of_column)

    def set_live(self, row, col, current=True):
        grid = self.grid if current else self.next_grid
        num_live_nb = self.num_live_neighbor if current else self.next_num_live_neighbor
        grid[row][col] = 1
        #for (i, j) in self.neighbors(row, col):
        #    num_live_nb[i][j] += 1

    def set_dead(self, row, col, current=True):
        grid = self.grid if current else self.next_grid
        num_live_nb = self.num_live_neighbor if current else self.next_num_live_neighbor
        grid[row][col] = 0
        for (i, j) in self.neighbors(row, col):
            assert num_live_nb[i][j] > 0
            num_live_nb[i][j] -= 1

    def neighbors(self, row, col):
        res = []
        min_row = row-1 if row>0 else row
        max_row = row+1 if row<len(self.grid)-1 else row
        min_col = col-1 if col>0 else col
        max_col = col+1 if col<len(self.grid[0])-1 else col
        for r in range(min_row, max_row+1):
            for c in range(min_col, max_col+1):
                if row != r or col != c:
                    res.append((r,c))
        return res

    def step(self):
        for r in len(self.grid):
            for c in len(self.grid):
                live = self.grid[r][c]
                if self.num_live_neighbor[r][c] == 3:
                    live = True
                elif self.num_live_neighbor[r][c] < 2 or self.num_live_neighbor[r][c] > 3:
                    live = False
                if live != self.grid[r][c]:
                    if live:
                        self.set_live(r, c, False)
                    else:
                        self.set_dead(r, c, False)
        self.grid = self.next_grid
        self.num_live_neighbor = self.next_num_live_neighbor

    def display(self):
        res = "   "
        for c in range(len(self.grid[0])):
            res += "%2d" % c
        res += "\n   "
        for c in range(len(self.grid[0])):
            res += "--"
        for r in range(len(self.grid)):
            res += "\n%d |" % (r)
            for c in range(len(self.grid[0])):
                res += "%2d" % self.grid[r][c]
        res += "\n"
        return res
