import unittest

from changes import *

class TestChanges(unittest.TestCase):
    def setUp(self):
        pass

    def check_solution(self, solution, expect_solution):
        self.assertEqual(len(solution), len(expect_solution))
        for s in solution:
            self.assertTrue(s in expect_solution)
        

    def test_basic(self):
        c = Changes([2, 5, 7])
        n = c.changes(6)
        self.check_solution(n, [[2, 2, 2]])
        n = c.changes(8)
        self.check_solution(n, [[2, 2, 2, 2]])
        n = c.changes(9)
        self.check_solution(n, [[2, 7], [2, 2, 5]])
        n = c.changes(10)
        self.check_solution(n, [[5, 5], [2, 2, 2, 2, 2]])
        n = c.changes(11)
        self.check_solution(n, [[2, 2, 7], [2, 2, 2, 5]])

if __name__ == "__main__":
    unittest.main()
