from rules_of_life import item_test
from list_implementation import *

class Life():
    def __init__(self, cells):
        self.life_grid = List()
        self.grid_lenth = 50
        self.grid_width = 50
        for i in xrange(self.grid_lenth):
            self.life_grid.append(List([False]*self.grid_width))
        for index_list in cells:
            self.life_grid[index_list[0]][index_list[1]] = True

    def start(self):
        j = 0
        k = 0
        for i in xrange(200):
            for sub_list in self.life_grid:
                for element in sub_list:
                    if element not False:
                        status = item_test(self.life_grid, j, k)
                        assert(status == True or status == False or status == None)
                        if status:
                            for neighbor in my_neighbors(j, k):
                                if neighbor == False:
                                    
                    j += 1
                k += 1

    def my_neighbors(self, row, col):
        neighbors = List()
        if is_corner(row, col):
            neighbors.append(row, col-1)
            neighbors.append(row+1, col-1)
            neighbors.append(row+1, col)

        type = is_border(row, col)
        elif type:
            if type == 1:
                neighbors.append(row+1, col)
                neighbors.append(row+1, col)
                neighbors.append(row+1, col)
                neighbors.append(row+1, col)
                neighbors.append(row+1, col)
                #change and finish my neighbors

        else:
            #not corner or border
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if i == row and j == col:
                        # do nothing for itself
                        pass
                    else:
                        neighbors.append([i, j])
        return neighbors

    def is_corner(row, col):
        if row == self.grid_lenth - 1 and col == self.grid_width - 1:
            return True
        return False

    def is_border(row, col):
        if row == self.grid_lenth - 1 or col == self.grid_width - 1:
            try:
                self.life_grid[row, col+1]
            except:
                return 1

            try:
                self.life_grid[row+1, col]
            except:
                return 2

            try:
                self.life_grid[row, col-1]
            except:
                return 3

            try:
                self.life_grid[row-1, col+1]
            except:
                return 4

            raise AssertionError

        return False
