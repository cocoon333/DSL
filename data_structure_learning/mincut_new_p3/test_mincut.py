import unittest
from mincut import *

class TestMinCut(unittest.TestCase):
    def setUp(self):
        pass

    def test_mincut_rec_basic_1(self):
        data = {1:[2], 2:[1]}
        mc = MinCut()
        self.assertEqual(mc._mincut_rec(data), 1)

    def test_mincut_rec_basic_2(self):
        data = {1:[2, 3], 2:[1], 3:[1]}
        mc = MinCut()
        self.assertEqual(mc._mincut_rec(data), 1)

    def test_mincut_rec_1(self):
        data = {1:[2], 2:[1, 3, 5], 3:[2, 4], 4:[3, 5], 5:[2, 4]}
        mc = MinCut()
        self.assertEqual(mc._mincut_rec(data), 2)

    def test_mincut_rec_2(self):
        data = {1:[2, 3, 4, 5], 2:[1, 3, 5], 3:[1, 2, 4], 4:[1, 3, 5], 5:[1, 2, 4]}
        mc = MinCut()
        self.assertEqual(mc._mincut_rec(data), 4)


    def test_mincut_2(self):
        data = {1:[2, 3, 4, 5], 2:[1, 3, 5], 3:[1, 2, 4], 4:[1, 3, 5], 5:[1, 2, 4]}
        mc = MinCut()
        self.assertEqual(mc.mincut(data), 3)
        
if __name__ == '__main__':
    unittest.main()
