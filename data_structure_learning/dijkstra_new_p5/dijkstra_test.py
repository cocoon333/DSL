import unittest
from dijkstra import *

class DijkstraTest(unittest.TestCase):
    def test_dijkstra_basic(self):
        d = Dijkstra()
        self.assertEqual(d.dijkstra([[1,1, 2,1], [0,1, 2,1], [0,1, 1,1]]), {0:0, 1:1, 2:1})

    def test_dijkstra(self):
        d = Dijkstra()
        data = [[2,1, 3,2], [3,1, 4,2], [0,1, 4,2], [0,1, 1,2], [1,1, 2,2]]
        self.assertEqual(d.dijkstra(data), {0:0, 1:4, 2:1, 3:2, 4:3})

    def test_dijkstra2(self):
        d = Dijkstra()
        data = [[1,1, 4,6], [0,1, 3,6, 2,4, 4,4], [1,4, 3,9, 4,8], [1,6, 2,9, 4,3], [0,6, 1,4, 2,8, 3,3]]
        self.assertEqual(d.dijkstra(data), {0: 0, 1: 1, 2: 5, 3: 7, 4: 5})

class HeapTest(unittest.TestCase):
    def setUp(self):
        self.h = Heap()

    def test_push(self):
        self.h.push(0, 0)
        self.assertEqual(self.h.h, [[0, 0]])

    def test_pop(self):
        self.h.push(0, 0)
        self.assertEqual(self.h.pop(), (0, 0))

    def test_delete(self):
        self.h.push(0, 0)
        self.h.delete(0)
        self.assertFalse(self.h.node_entry)

    def test_len(self):
        self.h.push(0, 0)
        self.assertEqual(len(self.h), 1)

    def test_contains(self):
        self.h.push(0, 0)
        self.assertTrue(0 in self.h)

    def test_getitem(self):
        self.h.push(0, 0)
        self.assertEqual(self.h[0], [0, 0])

if __name__ == "__main__":
    unittest.main()
