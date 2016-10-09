import unittest
from dijkstra import *

class DijkstraTest(unittest.TestCase):
    def test_calculate_key(self):
        d = Dijkstra([[1,10, 2,14], [0,14, 2,12], [0,14, 1,12]])
        visited_list = [(0, 0), (1, 10)]
        node = [0, 14, 1,12]
        self.assertEqual(d.calculate_key(visited_list, node), 14)

    def test_dijkstra(self):
        d = Dijkstra([[1,1, 2,1], [0,1, 2,1], [0,1, 1,1]])
        print d.dijkstra()


if __name__ == "__main__":
    unittest.main()
