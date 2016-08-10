from inc import inc, incrementer
import unittest

class IncTest(unittest.TestCase):
    def test_controller(self):
        i = inc([1, 2, 3])
        self.assertEqual(i.controller(), [1, 2, 4])
        i = inc([1, 2, 0])
        self.assertEqual(i.controller(), [1, 2, 1])
        i = inc([1, 9, 9])
        self.assertEqual(i.controller(), [2, 0, 0])

    def test_to_vec(self):
        i = incrementer()
        self.assertEqual(i.to_vec(100), [1, 0, 0])
        self.assertEqual(i.to_vec(229), [2, 2, 9])
        self.assertEqual(i.to_vec(000), [0])

    def test_inc(self):
        i = incrementer()
        self.assertEqual(i.inc(100), 101)
        self.assertEqual(i.inc(109), 110)
        self.assertEqual(i.inc(199), 200)
        self.assertEqual(i.inc(999), 1000)

if __name__ == '__main__':
    unittest.main()
