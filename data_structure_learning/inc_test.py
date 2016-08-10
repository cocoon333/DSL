from inc import inc
import unittest

class IncTest(unittest.TestCase):
    def test_controller(self):
        i = inc([1, 2, 3])
        self.assertEqual(i.controller(), [1, 2, 4])
        i = inc([1, 2, 0])
        self.assertEqual(i.controller(), [1, 2, 1])
        i = inc([1, 9, 9])
        self.assertEqual(i.controller(), [2, 0, 0])

if __name__ == '__main__':
    unittest.main()
