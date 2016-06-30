import unittest
from life import *

class TestLife(unittest.TestCase):
    def setUp(self):
        pass
    def test_display(self):
        l = Life()
        s = l.display()
        expr_s = """\
    0 1 2 3 4 5 6 7 8 9
    --------------------
0 | 0 0 0 0 0 0 0 0 0 0
1 | 0 0 0 0 0 0 0 0 0 0
2 | 0 0 0 0 0 0 0 0 0 0
3 | 0 0 0 0 0 0 0 0 0 0
4 | 0 0 0 0 0 0 0 0 0 0
5 | 0 0 0 0 0 0 0 0 0 0
6 | 0 0 0 0 0 0 0 0 0 0
7 | 0 0 0 0 0 0 0 0 0 0
8 | 0 0 0 0 0 0 0 0 0 0
9 | 0 0 0 0 0 0 0 0 0 0
"""
        #self.assertEqual(s, expr_s)
        pass

    def test_neighbors(self):
        l = Life()
        n = l.neighbors(0, 0)
        self.assertEqual(set(n), set([(0,1), (1,0), (1,1)]))
        n = l.neighbors(1, 0)
        self.assertEqual(set(n), set([(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)]))
        n = l.neighbors(5, 5)
        self.assertEqual(set(n), set([(4, 4), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4), (6, 5), (6, 6)]))
        n = l.neighbors(9, 5)
        self.assertEqual(set(n), set([(8, 4), (8, 5), (8, 6), (9, 4), (9, 6)]))

    def test_set_live(self):
        l = Life()
        l.set_live(0, 0, False)
        l.grid = l.next_grid
        for r in range(len(l.grid)):
            for c in range(len(l.grid[0])):
                if r == 0 and c == 0:
                    self.assertEqual(l.next_grid[r][c], 1)
                else:
                    self.assertEqual(l.next_grid[r][c], 0)


if __name__ == '__main__':
    unittest.main()
