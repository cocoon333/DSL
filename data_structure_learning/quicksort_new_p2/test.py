import unittest
from quicksort import *

class TestQuickSort(unittest.TestCase):
    def test_partition_1(self):
        qs = QuickSort()
        self.assertEqual(qs.partition([1, 2], 0, 1), 0)


    def test_partition_2(self):
        qs = QuickSort()
        self.assertEqual(qs.partition([1, 2, 3], 0, 2), 0)


    def test_partition_3(self):
        qs = QuickSort()
        self.assertEqual(qs.partition([2, 1, 3], 0, 2), 1)

    def test_partition_4(self):
        qs = QuickSort()
        self.assertEqual(qs.partition([3, 1, 2], 0, 2), 2)

    def test_sort_1(self):
        qs = QuickSort()
        data_ref = [1, 2]
        data = [1, 2]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)


    def test_sort_2(self):
        qs = QuickSort()
        data_ref = [1, 2, 3]
        data = [1, 2, 3]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 3)


    def test_sort_3(self):
        qs = QuickSort()
        data_ref = [1, 2, 3]
        data = [2, 1, 3]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 3)

    def test_sort_4(self):
        qs = QuickSort()
        data_ref = [1, 2, 3]
        data = [3, 1, 2]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 3)


if __name__ == '__main__':
        unittest.main()
        
