import unittest

from changes import *

class TestChanges(unittest.TestCase):
    def setUp(self):
        pass

    def test_basic(self):
        c = Changes([2, 5, 7])
        n = c.changes(6)
        self.assertEqual(set(n), set([2, 2, 2]))
        n = c.changes(8)
        self.assertEqual(set(n), set([2, 2, 2, 2]))
        n = c.changes(9)
        self.assertEqual(set(n), set([2, 7]))
        n = c.changes(10)
        self.assertEqual(set(n), set([5, 5]))
        n = c.changes(11)
        self.assertEqual(set(n), set([2, 2, 7]))

if __name__ == "__main__":
    unittest.main()
