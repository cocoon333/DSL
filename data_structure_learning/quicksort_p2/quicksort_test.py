import unittest
import copy
from quicksort import *

class QuicksortTest(unittest.TestCase):
    def test_quicksort(self):
        q = Quicksort()

        s = [1, 9, 7, 8, 10]
        #   [1, 9, 7, 8, 10]
        #   [x, 9, 7, 8, 10]
        exp = copy.deepcopy(s)
        exp.sort()
        self.assertEqual(q.quicksort(s), exp)

        s = [5, 3, 2, 4, 6, 1, 9, 7, 8, 10]
        #   [1, 3, 2, 4, 5, 6, 9, 7, 8, 10]
        #   [x, x, x, x, x, 6, 9, 7, 8, 10]
        #   [x, x, x, x, x, x, 9, 7, 8, 10]
        exp = copy.deepcopy(s)
        exp.sort()
        self.assertEqual(q.quicksort(s), exp)

        s = [12, 5, 3, 13, 2, 15, 4, 11, 6, 1, 14, 9, 7, 8, 10]
        exp  = copy.deepcopy(s)
        exp.sort()
        self.assertEqual(q.quicksort(s), exp)


        s = [5, 3, 2, 4, 1, 9, 8, 10]
        exp  = copy.deepcopy(s)
        exp.sort()
        self.assertEqual(q.quicksort(s), exp)


    def test_partition(self):
        q = Quicksort()
        self.assertEqual(q.partition([5, 2, 6, 1, 7, 3], 0, 5), 3)
        self.assertEqual(q.partition([6, 2, 5, 1, 7, 3], 0, 5), 4)
        self.assertEqual(q.partition([9, 7, 8, 10], 0, 3), 2)
        self.assertEqual(q.partition([5, 3, 2, 4, 6, 1, 9, 7, 8, 10], 6, 9), 8)

if __name__ == '__main__':
    unittest.main()
