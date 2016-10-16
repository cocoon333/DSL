import unittest
from quicksort import *

class TestQuickSort(unittest.TestCase):
    def test_partition_1(self):
        qs = QuickSort()
        self.assertEqual(qs.partition_method([1, 2], 0, 1), 0)


    def test_partition_2(self):
        qs = QuickSort()
        self.assertEqual(qs.partition_method([1, 2, 3], 0, 2), 0)


    def test_partition_3(self):
        qs = QuickSort()
        self.assertEqual(qs.partition_method([2, 1, 3], 0, 2), 1)

    def test_partition_4(self):
        qs = QuickSort()
        self.assertEqual(qs.partition_method([3, 1, 2], 0, 2), 2)

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
        self.assertEqual(qs.res, 2)

    def test_sort_4(self):
        qs = QuickSort()
        data_ref = [1, 2, 3]
        data = [3, 1, 2]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 3)
        
    def test_sort_5(self):
        qs = QuickSort()
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 45)


    def test_sort_6(self):
        qs = QuickSort()
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 1, 3, 5, 4, 6, 8, 7, 9, 10]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 30)

    def test_sort_7(self):
        qs = QuickSort()
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 45)

class TestQuickSortMethodLeft(unittest.TestCase):
    def test_partition_1(self):
        qs = QuickSort(partition_method=partition_left_pivot)
        self.assertEqual(qs.partition_method([1, 2], 0, 1), 0)


    def test_partition_2(self):
        qs = QuickSort(partition_method=partition_left_pivot)
        self.assertEqual(qs.partition_method([1, 2, 3], 0, 2), 0)


    def test_partition_3(self):
        qs = QuickSort(partition_method=partition_left_pivot)
        self.assertEqual(qs.partition_method([2, 1, 3], 0, 2), 1)

    def test_partition_4(self):
        qs = QuickSort(partition_method=partition_left_pivot)
        self.assertEqual(qs.partition_method([3, 1, 2], 0, 2), 2)

    def test_sort_1(self):
        qs = QuickSort(partition_method=partition_left_pivot)
        data_ref = [1, 2]
        data = [1, 2]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)


    def test_sort_2(self):
        qs = QuickSort(partition_method=partition_left_pivot)
        data_ref = [1, 2, 3]
        data = [1, 2, 3]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 3)


    def test_sort_3(self):
        qs = QuickSort(partition_method=partition_left_pivot)
        data_ref = [1, 2, 3]
        data = [2, 1, 3]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 2)

    def test_sort_4(self):
        qs = QuickSort(partition_method=partition_left_pivot)
        data_ref = [1, 2, 3]
        data = [3, 1, 2]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 3)
        
    def test_sort_5(self):
        qs = QuickSort(partition_method=partition_left_pivot)
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 45)


    def test_sort_6(self):
        qs = QuickSort(partition_method=partition_left_pivot)
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 1, 3, 5, 4, 6, 8, 7, 9, 10]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 30)

    def test_sort_7(self):
        qs = QuickSort(partition_method=partition_left_pivot)
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 45)

class TestQuickSortMethodRight(unittest.TestCase):
    def test_partition_1(self):
        qs = QuickSort(partition_method=partition_right_pivot)
        self.assertEqual(qs.partition_method([1, 2], 0, 1), 1)


    def test_partition_2(self):
        qs = QuickSort(partition_method=partition_right_pivot)
        self.assertEqual(qs.partition_method([1, 2, 3], 0, 2), 2)


    def test_partition_3(self):
        qs = QuickSort(partition_method=partition_right_pivot)
        self.assertEqual(qs.partition_method([2, 1, 3], 0, 2), 2)

    def test_partition_4(self):
        qs = QuickSort(partition_method=partition_right_pivot)
        self.assertEqual(qs.partition_method([3, 1, 2], 0, 2), 1)

    def test_sort_1(self):
        qs = QuickSort(partition_method=partition_right_pivot)
        data_ref = [1, 2]
        data = [1, 2]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)


    def test_sort_2(self):
        qs = QuickSort(partition_method=partition_right_pivot)
        data_ref = [1, 2, 3]
        data = [1, 2, 3]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 3)


    def test_sort_3(self):
        qs = QuickSort(partition_method=partition_right_pivot)
        data_ref = [1, 2, 3]
        data = [2, 1, 3]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 3)

    def test_sort_4(self):
        qs = QuickSort(partition_method=partition_right_pivot)
        data_ref = [1, 2, 3]
        data = [3, 1, 2]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 2)
        
    def test_sort_5(self):
        qs = QuickSort(partition_method=partition_right_pivot)
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 45)


    def test_sort_6(self):
        qs = QuickSort(partition_method=partition_right_pivot)
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 1, 3, 5, 4, 6, 8, 7, 9, 10]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 36)

    def test_sort_7(self):
        qs = QuickSort(partition_method=partition_right_pivot)
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 45)


class TestQuickSortMethodMedian3(unittest.TestCase):
    def test_get_pivot(self):
        data = [1, 2, 3]
        self.assertEqual(get_pivot_for_median_3(data, 0, 2), 1)

        data = [1, 3, 2]
        self.assertEqual(get_pivot_for_median_3(data, 0, 2), 2)

        data = [2, 1, 3]
        self.assertEqual(get_pivot_for_median_3(data, 0, 2), 0)

        data = [2, 3, 1]
        self.assertEqual(get_pivot_for_median_3(data, 0, 2), 0)

        data = [3, 2, 1]
        self.assertEqual(get_pivot_for_median_3(data, 0, 2), 1)

        data = [3, 1, 2]
        self.assertEqual(get_pivot_for_median_3(data, 0, 2), 2)

        data = [3, 2, 2]
        self.assertEqual(get_pivot_for_median_3(data, 0, 2), 1)

    def test_partition_1(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        self.assertEqual(qs.partition_method([1, 2], 0, 1), 0)


    def test_partition_2(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        self.assertEqual(qs.partition_method([1, 2, 3], 0, 2), 1)


    def test_partition_3(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        self.assertEqual(qs.partition_method([2, 1, 3], 0, 2), 1)

    def test_partition_4(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        self.assertEqual(qs.partition_method([3, 1, 2], 0, 2), 1)

    def test_sort_1(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2]
        data = [1, 2]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)


    def test_sort_2(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2, 3]
        data = [1, 2, 3]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 2)


    def test_sort_3(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2, 3]
        data = [2, 1, 3]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 2)

    def test_sort_4(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2, 3]
        data = [3, 1, 2]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 2)
        
    def test_sort_5(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 23)


    def test_sort_6(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 1, 3, 5, 4, 6, 8, 7, 9, 10]

    def test_partition_1(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        self.assertEqual(qs.partition_method([1, 2], 0, 1), 0)


    def test_partition_2(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        self.assertEqual(qs.partition_method([1, 2, 3], 0, 2), 1)


    def test_partition_3(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        self.assertEqual(qs.partition_method([2, 1, 3], 0, 2), 1)

    def test_partition_4(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        self.assertEqual(qs.partition_method([3, 1, 2], 0, 2), 1)

    def test_sort_1(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2]
        data = [1, 2]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)


    def test_sort_2(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2, 3]
        data = [1, 2, 3]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 2)


    def test_sort_3(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2, 3]
        data = [2, 1, 3]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 2)

    def test_sort_4(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2, 3]
        data = [3, 1, 2]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 2)
        
    def test_sort_5(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 19)


    def test_sort_6(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [2, 1, 3, 5, 4, 6, 8, 7, 9, 10]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 19)

    def test_sort_7(self):
        qs = QuickSort(partition_method=partition_median_3_pivot)
        data_ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        qs.quicksort(data)
        self.assertEqual(data, data_ref)
        self.assertEqual(qs.res, 19)



if __name__ == '__main__':
        unittest.main()
        
