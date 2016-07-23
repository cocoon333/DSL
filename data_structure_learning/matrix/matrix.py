import sys
sys.path.append("../")
from map_implementation import *
class SparseMatrix(object):
    def __init__(self, num_row, num_col):
        self.data = Map()
        assert (type(num_row) is int)
        assert (type(num_col) is int)
        assert (num_row > 0)
        assert (num_col > 0)
        self.num_row = num_row
        self.num_col = num_col

    def __getitem__(self, key):
        assert (type(key) == tuple)
        assert (len(key) == 2)
        if key in self.data:
            return self.data[key]
        else:
            return 0

    def __setitem__(self, key, value):
        assert (type(key) == tuple)
        assert (len(key) == 2)
        assert (type(value) == int)
        self.data[key] = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        res = "\n"
        for r in range(self.num_row):
            v_r = ""
            for c in range(self.num_col):
                v_r += str(self[(r,c)])
            res += v_r + "\n"
        return res

    def transport(self):
        res = SparseMatrix(num_row=self.num_col, num_col=self.num_row)
        for (k, v) in self.data.items():
            assert (type(k) is tuple)
            assert (len(k) == 2)
            assert (k[1], k[0]) not in res.data
            res[(k[1], k[0])] = v
        assert (len(res.data.keys()) == len(self.data.keys()))
        return res

    def __add__(self, m):
        res = SparseMatrix(num_row=self.num_row, num_col=self.num_col)
        assert (type(m) is SparseMatrix)
        for (k, v) in m.data.items():
            res[k] = m[k] + self[k]
        for (k, v) in self.data.items():
            res[k] = m[k] + self[k]
        return res


