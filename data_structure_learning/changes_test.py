import unittest
from changes import *

class ChangeTest(unittest.TestCase):
    def test_basic(self):
        c = Changes([2, 5, 7])
        self.assertEqual(set(c.changes(8)[0]), set([2, 2, 2, 2]))
        self.assertEqual(set(c.changes(9)[0]), set([2, 7, 2, 2, 7, 2]))
        self.assertEqual(set(c.changes(10)[0]), set([5, 5]))
        self.assertEqual(set(c.changes(11)[0]), set([7, 2, 2]))
        self.assertEqual(set(c.changes(12)[0]), set([7, 5]))

    def test_enum_changes(self):
        e = EnumChanges([2, 5, 7])
        e8 = e.changes(8)
        e9 = e.changes(9)
        e8.sort()
        e9.sort()
        self.assertEqual(e8, [[2, 2, 2, 2]])
        self.assertEqual(e9, [[2, 2, 5], [2, 5, 2], [2, 7], [5, 2, 2]])
        self.assertEqual(set(e.changes(10)[0]), set([5, 5]))
        self.assertEqual(set(e.changes(11)[0]), set([7, 2, 2]))
        self.assertEqual(set(e.changes(12)[0]), set([7, 5]))


if __name__ == '__main__':
    unittest.main()
