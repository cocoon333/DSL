import unittest
from inversion import *

class InversionTest(unittest.TestCase):
    def test_merge(self):
        i = Inversion()
        l = [1, 2, 3, 4, 5]
        l1 =[3, 4, 5, 1, 2]
        self.assertEqual(i.merge_method(l, 0, 2, 4), 0)
        self.assertEqual(i.merge_method(l1, 0, 2, 4), 6)
        self.assertEqual(l, [1, 2, 3, 4, 5])
        self.assertEqual(l1, l)

    def test_merge_basic(self):
        i = Inversion()
        l = [1, 2]
        l1 =[2, 1]
        self.assertEqual(i.merge_method(l, 0, 0, 1), 0)
        self.assertEqual(i.merge_method(l1, 0, 0, 1), 1)
        self.assertEqual(l, [1, 2])
        self.assertEqual(l1, l)

    def test_calculate_rec(self):
        i = Inversion()
        l = [1, 2, 3, 4, 5]
        l1 =[5, 4, 3, 2, 1]
        self.assertEqual(i.calculate_rec(l, 0, 4), 0)
        self.assertEqual(i.calculate_rec(l1, 0, 4), 10)
        self.assertEqual(l, [1, 2, 3, 4, 5])
        self.assertEqual(l1, l)

    def test_calculate_rec_basic(self):
        i = Inversion()
        l = [1, 2]
        l1 =[2, 1]
        self.assertEqual(i.calculate_rec(l, 0, 1), 0)
        self.assertEqual(i.calculate_rec(l1, 0, 1), 1)
        self.assertEqual(l, [1, 2])
        self.assertEqual(l1, l)

    def test_calculate(self):
        i = Inversion()
        l = [1, 2, 3, 4, 5]
        l1 =[5, 4, 3, 2, 1]
        self.assertEqual(i.calculate(l), 0)
        self.assertEqual(i.calculate(l1), 10)

class InversionNewTest(unittest.TestCase):
    def test_merge_new(self):
        i = Inversion(merge_method=merge_new)
        l = [1, 2, 3, 4, 5]
        l1 =[3, 4, 5, 1, 2]
        self.assertEqual(i.merge_method(l, 0, 2, 4), 0)
        self.assertEqual(i.merge_method(l1, 0, 2, 4), 6)
        self.assertEqual(l, [1, 2, 3, 4, 5])
        self.assertEqual(l1, l)

    def test_merge_new_basic(self):
        i = Inversion(merge_method=merge_new)
        l = [1, 2]
        l1 =[2, 1]
        self.assertEqual(i.merge_method(l, 0, 0, 1), 0)
        self.assertEqual(i.merge_method(l1, 0, 0, 1), 1)
        self.assertEqual(l, [1, 2])
        self.assertEqual(l1, l)

    def test_calculate_new_rec(self):
        i = Inversion(merge_method=merge_new)
        l = [1, 2, 3, 4, 5]
        l1 =[5, 4, 3, 2, 1]
        self.assertEqual(i.calculate_rec(l, 0, 4), 0)
        self.assertEqual(i.calculate_rec(l1, 0, 4), 10)
        self.assertEqual(l, [1, 2, 3, 4, 5])
        self.assertEqual(l1, l)

    def test_calculate_new_rec_basic(self):
        i = Inversion(merge_method=merge_new)
        l = [1, 2]
        l1 =[2, 1]
        self.assertEqual(i.calculate_rec(l, 0, 1), 0)
        self.assertEqual(i.calculate_rec(l1, 0, 1), 1)
        self.assertEqual(l, [1, 2])
        self.assertEqual(l1, l)

    def test_calculate_new(self):
        i = Inversion(merge_method=merge_new)
        l = [1, 2, 3, 4, 5]
        l1 =[5, 4, 3, 2, 1]
        self.assertEqual(i.calculate(l), 0)
        self.assertEqual(i.calculate(l1), 10)



if __name__ == "__main__":
    unittest.main()
