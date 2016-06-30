import unittest
from life import Life
from rules_of_life import *
from list_implementation import List

class TestLife(unittest.TestCase):
    def test_rules(self):
        array = List()
        for i in xrange(50):
            array.append(List([False]*50))
        self.assertFalse(item_test(array, 0, 0))
        array[1][0] = True
        array[0][1] = True
        self.assertEqual(item_test(array, 0, 0), 1)
        array[1][1] = True
        self.assertTrue(item_test(array, 0, 0))

    def test_my_neighbors(self):
        array = List()
        for i in xrange(50):
            array.append(List([False]*50))
        self.assertEqual(my_neighbors(array, 0, 0)[0:3], [[0, 1], [1, 1], [1, 0]][0:3])
        self.assertEqual(my_neighbors(array, 49, 0)[0:3], [[48, 0], [48, 1], [49, 1]][0:3])
        self.assertEqual(my_neighbors(array, 0, 49)[0:3], [[0, 48], [1, 48], [1, 49]][0:3])
        self.assertEqual(my_neighbors(array, 49, 49)[0:3], [[49, 48], [48, 48], [48, 49]][0:3])

        self.assertEqual(my_neighbors(array, 7, 49)[0:5], [[6, 49], [6, 48], [7, 48], [8, 48], [8, 49]])
        self.assertEqual(my_neighbors(array, 49, 7)[0:5], [[49, 8], [48, 8], [48, 7], [48, 6], [49, 6]])
        self.assertEqual(my_neighbors(array, 7, 0)[0:5], [[8, 0], [8, 1], [7, 1], [6, 1], [6, 0]])
        self.assertEqual(my_neighbors(array, 0, 7)[0:5], [[0, 6], [1, 6], [1, 7], [1, 8], [0, 8]])

    def test_corner(self):
        array = List()
        for i in xrange(50):
            array.append(List([False]*50))
        self.assertEqual(is_corner(array, 0, 0), 1)
        self.assertEqual(is_corner(array, 49, 0), 2)
        self.assertEqual(is_corner(array, 49, 49), 3)
        self.assertEqual(is_corner(array, 0, 49), 4)
        self.assertFalse(is_corner(array, 5, 5))

    def test_border(self):
        array = List()
        for i in xrange(50):
            array.append(List([False]*50))
        self.assertEqual(is_border(array, 7, 49), 1)
        self.assertEqual(is_border(array, 49, 8), 2)
        self.assertEqual(is_border(array, 4, 0), 3)
        self.assertEqual(is_border(array, 0, 19), 4)
        self.assertFalse(is_border(array, 5, 5))

    def test_life(self):
        l = Life()
        l.start(1, 0)
        for sublist in l.life_grid:
            for element in sublist:
                self.assertFalse(element)
        for i in xrange(2, 11):
            l.start(1, 0)
            for sublist in l.life_grid:
                for element in sublist:
                    self.assertFalse(element)
        for i in xrange(10):
            l.start(10, 0)
            for sublist in l.life_grid:
                for element in sublist:
                    self.assertFalse(element)

if __name__ == '__main__':
    unittest.main()
