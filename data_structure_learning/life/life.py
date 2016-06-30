from rules_of_life import *
from list_implementation import *
import time

class Life():
    def __init__(self, cells=[]):
        self.grid_width = 10
        self.grid_lenth = 10
        self.life_grid = List()
        for i in xrange(self.grid_lenth):
            self.life_grid.append(List([0]*self.grid_width))
        for index_list in cells:
            self.life_grid[index_list[0]][index_list[1]] = 1

    def start(self, iteration_times=200, wait_time=0):
        for i in xrange(iteration_times):
            next_cycle = List()
            for i in xrange(self.grid_lenth):
                next_cycle.append(List([0]*self.grid_width))
            j = 0
            for sub_list in self.life_grid:
                k = 0
                for element in sub_list:
                    assert(j < 10)
                    assert (k < 10)
                    status = item_test(self.life_grid, j, k)
                    if status == 2:
                        next_cycle[j][k] = 1
                    if not status:
                        next_cycle[j][k] = 0
                    if status == 1:
                        next_cycle[j][k] = self.life_grid[j][k]
                    k += 1
                j += 1
            self.life_grid = next_cycle
            print self.life_grid
            print '\n'
            time.sleep(wait_time)
