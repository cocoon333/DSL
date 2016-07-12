import unittest

from matrix import *


class TestMatrix(unittest.TestCase):
    def setUp(self):
        pass

    def test_basic(self):
        m = SparseMatrix(2, 2)
        self.assertEqual(str(m), "\n00\n00\n")


    def test_change(self):
        m = SparseMatrix(2, 2)
        self.assertEqual(str(m), "\n00\n00\n")
        m[(0, 0)] = 2
        self.assertEqual(m[(0, 0)], 2)
        self.assertEqual(m[(0, 1)], 0)
        self.assertEqual(str(m), "\n20\n00\n")

    def test_transport(self):
        m = SparseMatrix(2, 3)
        self.assertEqual(str(m), "\n000\n000\n")
        m1 = m.transport()
        self.assertEqual(str(m1), "\n00\n00\n00\n")
        m[(0, 0)]  = 2
        m[(1, 0)]  = 3
        self.assertEqual(str(m), "\n200\n300\n")
        m1 = m.transport()
        self.assertEqual(str(m1), "\n23\n00\n00\n")


    def test_add(self):
        m = SparseMatrix(2, 3)
        m[(0, 0)]  = 2
        m[(1, 0)]  = 3
        self.assertEqual(str(m), "\n200\n300\n")
        m1 = SparseMatrix(2, 3)
        m1[(0, 0)]  = 4
        m1[(0, 1)]  = 5
        self.assertEqual(str(m1), "\n450\n000\n")
        m2 = m + m1
        self.assertEqual(str(m2), "\n650\n300\n")


if __name__ == '__main__':
    unittest.main()
