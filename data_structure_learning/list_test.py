import unittest
from list_implementation import *

class ListTest(unittest.TestCase):
    def setUp(self):
        self.list = List()
        self.list.append('sister')
        self.list.append('is')
        self.list.append('stupid')
        self.list.append('smart')
        self.list.append('hi')
        self.list.append('world')

    def test_len(self):
        self.assertEqual(len(self.list), 6)
        self.list.append(1)
        self.assertEqual(len(self.list), 7)

    def test_contains(self):
        self.assertTrue('sister' in self.list)
        self.assertFalse(1 in self.list)

    def test_append(self):
        self.assertEqual(self.list.lyst[0], 'sister')
        self.assertEqual(self.list.lyst[1], 'is')
        self.assertEqual(self.list.lyst[2], 'stupid')
        self.assertEqual(self.list.lyst[3], 'smart')
        self.assertEqual(self.list.lyst[4], 'hi')
        self.assertEqual(self.list.lyst[5], 'world')

    def test_remove(self):
        self.list.remove('stupid')
        self.assertEqual(len(self.list), 5)
        self.assertFalse('stupid' in self.list)

    def test_index(self):
        self.assertEqual(self.list.index('sister'), 0)
        self.assertEqual(self.list.index('is'), 1)
        self.assertEqual(self.list.index('stupid'), 2)
        self.assertEqual(self.list.index('smart'), 3)
        self.assertEqual(self.list.index('hi'), 4)
        self.assertEqual(self.list.index('world'), 5)

    def test_count(self):
        self.assertEqual(self.list.count('sister'), 1)

if __name__ == '__main__':
    unittest.main()
