class Changes(object):
    def __init__(self, coins):
        assert (type(coins) == list)
        for c in coins:
            assert (type(c) == int and c > 0)
        self.coins = coins
        self.coins.sort(reverse=True)

    def changes(self, N):
        assert (N > 0)
        solution = []
        if self.changes_rec(N, solution):
            assert (solution)
            assert (sum(solution) == N)
            return solution
        else:
            return None

    def changes_rec(self, N, solution):
        assert (N >= 0)
        if N == 0:
            return True
        else:
            for i in self.coins:
                if i <= N:
                    if (self.changes_rec(N-i, solution)):
                        solution.append(i)
                        return True
        return False
