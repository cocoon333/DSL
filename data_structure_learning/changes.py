class Change(object):
    def __init__(self, coins):
        assert(type(coins) == list)
        for i in coins:
            assert(type(i) == int and i >= 0)
        self.coins = coins
        self.coins.sort(reverse=True)

    def change(self, N):
        solution = []
        for i in xrange(N/2):
            solution.append([])
        if self.change_rec(N, solution):
            return solution
        else:
            return None

    def change_rec(self, N, solution, k=0):
        j = 0
        assert(N >= 0)
        if N == 0:
            return True
        else:
            for i in self.coins:
                if i <= N:
                    if self.change_rec(N-i, solution, k+1):
                        solution[0].append(i)
                        if k != 0:
                            return True
                        else:
                            assert(k == 0)
                            self.change_rec(N, solution)
                j += 1
        if not solution[0]:
            return False
        else:
            return True
