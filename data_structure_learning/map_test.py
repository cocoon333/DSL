import unittest
from map_implementation import Map
from set_implementation import Set

class MapTest(unittest.TestCase):
    def setUp(self):
        self.map = Map()
        self.map.add(['lucy', 'sister'])
        self.map.add(['ruoxi', 'awesome'])
        self.map.add(['cici', 'bad'])

    def test_len(self):
        self.assertEqual(len(self.map), 3)
        self.map.add(['a', 'b'])
        self.assertEqual(len(self.map), 4)

    def test_contains(self):
        self.assertTrue('cici' in self.map)
        self.assertFalse('a' in self.map)

    def test_equal(self):
        compare_map = Map()
        compare_map.add(['lucy', 'sister'])
        compare_map.add(['ruoxi', 'awesome'])
        compare_map.add(['cici', 'bad'])
        self.assertTrue(compare_map == self.map)
        compare_map.add(['s', 'd'])
        self.assertFalse(compare_map == self.map)

    def test_add(self):
        self.assertFalse('liuruoxi' in self.map)
        self.map.add(['liuruoxi', 'funny'])
        self.assertTrue('liuruoxi' in self.map)

    def test_union(self):
        self.maxDiff = None
        m = Map()
        m.add(['Conner', 'Best'])
        merge = m + self.map
        l = [['Conner', 'Best'], ['lucy', 'sister'], ['ruoxi', 'awesome'], ['cici', 'bad']]
        for (k, v) in l:
            self.assertTrue(k in merge)
            self.assertTrue(merge.get(k) == v)

    def test_clear(self):
        self.map.clear()
        self.assertFalse(self.map.map)

    def test_get(self):
        self.assertEqual(self.map.get('cici'), 'bad')

    def test_has_key(self):
        self.assertTrue(self.map.has_key('cici'))
        self.assertFalse(self.map.has_key('hi'))

    def test_items(self):
        self.assertEqual(self.map.items().sort(), ['sister', 'awesome', 'bad'].sort())

    def test_keys(self):
        self.assertEqual(self.map.keys().sort(), ['lucy', 'ruoxi', 'cici'].sort())

    def test_remove(self):
        self.map.remove('cici')
        l = ['sister', 'awesome']
        s1 = Set()
        s2 = Set()
        [s1.add(x) for x in l]
        [s2.add(x) for x in self.map.items()]
        self.assertEqual(s1, s2)

    def test_hash(self):
        self.assertEqual(self.map.hash(10, 10), 0)
        self.assertEqual(self.map.hash(5, 4), 1)
        self.assertEqual(self.map.hash(2, 9), 2)

if __name__ == '__main__':
    unittest.main()
