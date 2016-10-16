import unittest
from scc3 import *

class SCCTest(unittest.TestCase):
    def test_reverse(self):
        scc = SCC()
        self.assertEqual(scc.reverse([[1], [2], [0]]), [[2], [0], [1]])

    def test_dfs_cf_basic(self):
        scc = SCC()
        d = {}
        i = [0]
        visited_nodes = set()
        scc.dfs_cf([[2], [0], [1]], 2, visited_nodes, d)
        self.assertEqual(d, {0: 0, 1: 1, 2: 2})

    def test_dfs_cf(self):
        scc = SCC()
        finish_time_dictionary = {}
        i = [0]
        data_r = [[1], [2], [3], [0, 4], [5], [6], []]
        visited_nodes = set()
        scc.dfs_cf(data_r, 0, visited_nodes, finish_time_dictionary)
        self.assertEqual(finish_time_dictionary, {0: 6, 1: 5, 2: 4, 3: 3, 4: 2, 5: 1, 6: 0})

    def test_dfs_cl_basic(self):
        scc = SCC()
        d = {}
        i = [0]
        data = [[1], [2], [0]]
        visited_nodes = set()
        scc.dfs_cl(data, 2, visited_nodes, 2, d)
        self.assertEqual(d, {2:[2, 0, 1]})

    def test_dfs_cl(self):
        scc = SCC()
        d = {}
        i = [0]
        data = [[1], [2], [3], [0, 4], [5], [6], []]
        visited_nodes = set()
        scc.dfs_cl(data, 0, visited_nodes, 0, d)
        self.assertEqual(d, {0: [0, 1, 2, 3, 4, 5, 6]})

    def test_scc_basic(self):
        scc = SCC()
        res = scc.scc([[0, 1], [1, 2], [2, 0]])
        self.assertEqual(res, {2: [2, 0, 1]})

    def test_scc(self):
        scc = SCC()
        data = [[1], [2], [3], [0, 4], [5], [6], []]
        res = scc.scc(data)
        self.assertEqual(res, {3: [3, 0, 1, 2], 4: [4], 5: [5], 6: [6]})

if __name__ == "__main__":
    unittest.main()
