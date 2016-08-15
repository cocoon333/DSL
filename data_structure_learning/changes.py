import copy 
from inc import *

class Changes(object):
    def __init__(self, coins):
        assert(type(coins) == list)
        for i in coins:
            assert(type(i) == int and i >= 0)
        self.coins = coins
        self.coins.sort(reverse=True)

    def changes(self, N):
        solution = []
        final_solution = []
        self.changes_rec(N, solution, final_solution)
        if final_solution[0]:
            for s in final_solution:
                assert (sum(s) == N)
        solution_list = []
        #FIXME: need use hash to solve the performance problem
        for s in final_solution:
            s.sort()
            if s not in solution_list:
                solution_list.append(s)
        return solution_list

    def changes_rec(self, N, solution, final_solution):
        assert(N >= 0)
        if N == 0:
            final_solution.append(copy.deepcopy(solution))
        else:
            for i in self.coins:
                if i <= N:
                    solution.append(i)
                    self.changes_rec(N-i, solution, final_solution)
                    solution.pop()

class EnumChanges(object):
    def __init__(self, coins):
        for i in coins:
            assert(type(i) == int and i >= 0)
        self.coins = coins
        self.coins.sort(reverse=True)
        self.depth = 0
        self.layer = []

    def changes(self, N):
        res = []
        combinations = []
        i = incrementer()
        l = i.vec_to_int(self.layer)
        increased = []

        self.depth = (N-1)/2 + 1
        while len(increased) <= self.depth:
            increased = i.to_vec(i.inc(l, len(self.coins)))
            l = i.inc(l, len(self.coins))
            combinations.append(increased)
        

        for element in combinations:
            s = 0
            res.append([])
            for i in element:
                res[-1].append(self.coins[i])
                s += self.coins[i]
            if s != N:
                del res[-1]
        return res
