import unittest
from changes import *

class ChangeTest(unittest.TestCase):
    def test_basic(self):
        c = Change([2, 5, 7])
        print c.change(10)
        print c.change(11)
        print c.change(12)
        self.assertEqual(set(c.change(8)[0]), set([2, 2, 2, 2]))
        self.assertEqual(set(c.change(9)[0]), set([2, 7, 2, 2, 5, 7, 2]))
        self.assertEqual(set(c.change(10)[0]), set([5, 5]))
        self.assertEqual(set(c.change(11)[0]), set([7, 2, 2]))
        self.assertEqual(set(c.change(12)[0]), set([7, 5]))

if __name__ == '__main__':
    unittest.main()
