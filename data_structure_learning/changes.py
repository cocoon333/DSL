import copy 

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
        self.depth = (N-1)/2 + 1
        self.layer = [0]*self.depth
        while self.layer[0] <= 3:
            res.append(copy.deepcopy(solution))
            self.inc()

    def inc(self):
        

            
