import unittest
from map_implementation import Map

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
        self.assertTrue(['cici', 'bad'] in self.map)
        self.assertFalse(['a', 'b'] in self.map)

    def test_equal(self):
        compare_map = Map()
        compare_map.add(['lucy', 'sister'])
        compare_map.add(['ruoxi', 'awesome'])
        compare_map.add(['cici', 'bad'])
        self.assertTrue(compare_map == self.map)
        compare_map.add(['s', 'd'])
        self.assertFalse(compare_map == self.map)

    def test_add(self):
        self.assertEqual(self.map.map, [['lucy', 'sister'], ['ruoxi', 'awesome'], ['cici', 'bad']])
        self.map.add(['liuruoxi', 'funny'])
        self.assertNotEqual(self.map.map, [['lucy', 'sister'], ['ruoxi', 'awesome'], ['cici', 'bad']])

    def test_union(self):
        m = Map()
        m.add(['Conner', 'Best'])
        merge = m + self.map
        self.assertEqual(merge.map, [['Conner', 'Best'], ['lucy', 'sister'], ['ruoxi', 'awesome'], ['cici', 'bad']])

    def test_clearsub_list(self):
        self.map.clear()
        self.assertFalse(self.map.map)

    def test_get(self):
        self.assertEqual(self.map.get('cici'), 'bad')

    def test_has_key(self):
        self.assertTrue(self.map.has_key('cici'))
        self.assertFalse(self.map.has_key('hi'))

    def test_items(self):
        self.assertEqual(self.map.items(), ['sister', 'awesome', 'bad'])

    def test_keys(self):
        self.assertEqual(self.map.keys(), ['lucy', 'ruoxi', 'cici'])

    def test_remove(self):
        self.map.remove('cici')
        self.assertEqual(self.map.items(), ['sister', 'awesome'])

if __name__ == '__main__':
    unittest.main()
