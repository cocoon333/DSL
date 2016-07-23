import unittest
from map_implementation import Map
from set_implementation import Set

class MapTest(unittest.TestCase):
    def setUp(self):
        self.map = Map()
        self.map['lucy'] = 'sister'
        self.map['cici'] = 'bad'
        self.map['ruoxi'] = 'awesome'
    
    def test_set_item(self):
        status = 0
        for sub_list in self.map.map:
            for pair in sub_list:
                if pair == ['lucy', 'sister'] or pair == ['cici', 'bad'] or pair == ['ruoxi', 'awesome']:
                    status += 1
        self.assertEqual(status, 3)

    def test_len(self):
        self.assertEqual(len(self.map), 3)
        self.map['a'] = 'b'
        self.assertEqual(len(self.map), 4)

    def test_contains(self):
        self.assertTrue('cici' in self.map)
        self.assertFalse('a' in self.map)

    def test_equal(self):
        compare_map = Map()
        compare_map['lucy'] = 'sister'
        compare_map['cici'] = 'bad'
        compare_map['ruoxi'] = 'awesome'
        self.assertTrue(compare_map == self.map)
        compare_map['s'] = 'd'
        self.assertFalse(compare_map == self.map)

    def test_add(self):
        self.assertFalse('liuruoxi' in self.map)
        self.map['liuruoxi'] = 'funny'
        self.assertTrue('liuruoxi' in self.map)

    def test_union(self):
        m = Map()
        m['Conner'] = 'Best'
        merge = m + self.map
        l = [['Conner', 'Best'], ['lucy', 'sister'], ['ruoxi', 'awesome'], ['cici', 'bad']]
        for (k, v) in l:
            self.assertTrue(k in merge)
            self.assertTrue(merge[k] == v)

    def test_clear(self):
        self.map.clear()
        self.assertTrue(len(self.map.map),  50)

    def test_get(self):
        self.assertEqual(self.map['cici'], 'bad')

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
        self.assertEqual(self.map.hash(10), 10)
        self.assertEqual(self.map.hash(5), 5)
        self.assertEqual(self.map.hash(2), 2)
        self.assertEqual(self.map.hash('abc'), 44)
if __name__ == '__main__':
    unittest.main()
