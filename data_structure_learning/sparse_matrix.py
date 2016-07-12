import unittest
from pro20_chpt4_SparseMatrix_functions import *

class MatrixTest(unittest.TestCase):
    def test_transpose(self):
        sm = SparseMatrix([[1, [1, 1]], [2, [2, 2]], [3, [3, 3]], [4, [4, 4]]])
        sm.transpose()
        a = []
        for item in sm.value_list:
            a.append(item)
        self.assertEqual(a, [[1, [1, 1]], [2, [2, 2]], [3, [3, 3]], [4, [4, 4]]])
        sm = SparseMatrix([[1, [1, 2]], [2, [2, 3]], [3, [3, 4]], [4, [4, 5]]])
        sm.transpose()
        a = []
        for item in sm.value_list:
            a.append(item)
        self.assertEqual(a, [[1, [2, 1]], [2, [3, 2]], [3, [4, 3]], [4, [5, 4]]])

    def test_get_item(self):
        sm = SparseMatrix([[1, [1, 1]]])
        self.assertEqual(sm[1, 1], 1)

    def test_set_item(self):
        sm = SparseMatrix([[1, [1, 1]]])
        sm[1, 1] = 2
        self.assertEqual(sm[1, 1], 2)

    def test_subtract(self):
        sm1 = SparseMatrix([[5, [1, 1]]])
        sm2 = SparseMatrix([[5, [1, 1]]])
        sm1.subtract(sm2.value_list)
        self.assertEqual(sm1[1, 1], 0)
        sm1 = SparseMatrix([])
        sm2 = SparseMatrix([[5, [1, 1]]])
        sm1.subtract(sm2.value_list)
        self.assertEqual(sm1[1, 1], -5)
        sm1 = SparseMatrix([[5, [1, 1]]])
        sm2 = SparseMatrix([[2, [1, 1]]])
        sm1.subtract(sm2.value_list)
        self.assertEqual(sm1[1, 1], 3)

    def test_multiply(self):
        sm1 = SparseMatrix([[5, [1, 1]]])
        sm2 = SparseMatrix([[6, [6, 1]]])
        sm1.multiplay(sm2.value_list)
        self.assertEqual(sm1[1, 1], 30)

    def test_subtract(self):
        sm1 = SparseMatrix([[5, [1, 1]]])
        sm2 = SparseMatrix([[5, [1, 1]]])
        sm1.add(sm2.value_list)
        self.assertEqual(sm1[1, 1], 10)
        sm1 = SparseMatrix([])
        sm2 = SparseMatrix([[5, [1, 1]]])
        sm1.add(sm2.value_list)
        self.assertEqual(sm1[1, 1], 5)
        sm1 = SparseMatrix([[5, [1, 1]]])
        sm2 = SparseMatrix([[-5, [1, 1]]])
        sm1.add(sm2.value_list)
        self.assertEqual(sm1[1, 1], 0)


if __name__ == '__main__':
    unittest.main()
