import unittest
from median import *

class MedianTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_median_1(self):
        m = Median()
        data = [0, 2, 1, 5, 3]
        correct_res = [0, 0, 1, 1, 2]
        for i in xrange(len(data)):
            self.assertEqual(m.get_median(data[i]), correct_res[i])
            
    def test_median_2(self):
        m = Median()
        data = [0,  1, 2, 3, 5]
        correct_res = [0, 0, 1, 1, 2]
        for i in xrange(len(data)):
            self.assertEqual(m.get_median(data[i]), correct_res[i])
          
    def test_median_3(self):
        m = Median()
        data = [7, 3, 5, 1, 8, 4, 2]
        correct_res = [7, 3, 5, 3, 5, 4, 4]
        for i in xrange(len(data)):
            self.assertEqual(m.get_median(data[i]), correct_res[i])


    def test_median_4(self):
        m = Median()
        data = [6331, 2793, 1640, 9290, 225, 625, 6195, 2303, 5685, 1354]
        correct_res = [6331, 2793, 2793, 2793, 2793, 1640, 2793, 2303, 2793, 2303]
        for i in xrange(len(data)):
            self.assertEqual(m.get_median(data[i]), correct_res[i])



if __name__ == "__main__":
    unittest.main()
