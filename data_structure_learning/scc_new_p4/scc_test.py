import unittest
from scc import *

class SCCTest(unittest.TestCase):
    def test_dfs_ft(self):
        scc = SCC()
        vn = set()
        finish_time_map = {}
        data = [[1], [2], [0]]
        scc.dfs_ft(data, 2, vn, finish_time_map)
        self.assertEqual(finish_time_map, {1:0, 0:1, 2:2})


    def test_dfs_cl(self):
        scc = SCC()
        vn = set()
        leader_map = {}
        data = [[1], [2], [0]]
        scc.dfs_cl(data, 2, vn, 2, leader_map)
        self.assertEqual(leader_map, {2:[2, 0, 1]})

    def test_reverse(self):
        scc = SCC()
        data = [[1], [2], [0]]
        res = scc.reverse(data)
        self.assertEqual(res, [[2], [0], [1]])

    def test_scc(self):
        scc = SCC()
        data = [[1], [2], [0]]
        res = scc.scc(data)
        self.assertEqual(res, [[1], [2], [0]])

if __name__ == "__main__":
    unittest.main()
