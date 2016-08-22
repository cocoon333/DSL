import unittest
from quicksort import *

class QuicksortTest(unittest.TestCase):
    def test_quicksort(self):
        q = Quicksort()
        print q.quicksort([5, 3, 2, 4, 6, 1, 9, 7, 8, 10])
        print q.quicksort([12, 5, 3, 13, 2, 15, 4, 11, 6, 1, 14, 9, 7, 8, 10])
        print q.quicksort([5, 3, 2, 4, 1, 9, 8, 10])

    def test_partition(self):
        q = Quicksort()
        print q.partition([5, 2, 6, 1, 7, 3], 5)

if __name__ == '__main__':
    unittest.main()
