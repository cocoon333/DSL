import timeit
import unittest
from map_implementation import Map
from set_implementation import Set

class MapTest(unittest.TestCase):
    def setUp(self):
        self.map = Map()
        self.map['lucy'] = 'sister'
        self.map['cici'] = 'bad'
        self.map['ruoxi'] = 'awesome'

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
        self.assertEqual(self.map.hash(10, 10), 0)
        self.assertEqual(self.map.hash(5, 4), 1)
        self.assertEqual(self.map.hash(2, 9), 2)
s = Map()
s[1] = [1]
def test_1():
    len(s)

s1 = Map()
for i in xrange(10):
    s1[i] = i
def test_2():
    len(s1)

s2 = Map()
for i in xrange(100):
    s2[i] = i
def test_3():
    len(s2)

s3 = Map()
for i in xrange(1000):
    s3[i]=[i]
def test_4():
    len(s3)

s4 = Map()
for i in xrange(10000):
    s4[i]=[i]
def test_5():
    len(s4)

s5 = Map()
for i in xrange(2000):
    s5[i] = i
def test_6():
    len(s5)

s6 = Map()
for i in xrange(3000):
    s6[i] = i
def test_7():
    len(s6)

s7 = Map()
for i in xrange(4000):
    s7[i]=[i]
def test_8():
    len(s7)

s8 = Map()
for i in xrange(5000):
    s8[i]=[i]
def test_9():
    len(s8)

s9 = Map()
for i in xrange(6000):
    s9[i] = i
def test_10():
    len(s9)

s15 = Map()
for i in xrange(7000):
    s15[i] = i
def test_16():
    len(s15)

s16 = Map()
for i in xrange(8000):
    s16[i]=[i]
def test_17():
    len(s16)

s17 = Map()
for i in xrange(9000):
    s17[i]=[i]
def test_18():
    len(s17)
print ''

s10 = Map()
s[10]=[10]
def test_11():
    1 in s10

s11 = Map()
for i in xrange(10):
    s11[i]=[i]
def test_12():
    10 in s13

s12 = Map()
for i in xrange(100):
    s12[i]=[i]
def test_13():
    100 in s12

s13 = Map()
for i in xrange(1000):
    s13[i]=[i]
def test_14():
    1000 in s13

s14 = Map()
for i in xrange(10000):
    s14[i]=[i]
def test_15():
    10000 in s14

s22 = Map()
for i in xrange(2000):
    s22[i] = [i]
def test_23():
    1 in s17

s18 = Map()
for i in xrange(3000):
    s18[i]=[i]
def test_19():
    10 in s18

s19 = Map()
for i in xrange(4000):
    s19[i]=[i]
def test_20():
    100 in s19

s20 = Map()
for i in xrange(5000):
    s20[i]=[i]
def test_21():
    1000 in s21

s21 = Map()
for i in xrange(6000):
    s21[i]=[i]
def test_22():
    10000 in s21

s23 = Map()
for i in xrange(7000):
    s23[i]=[i]
def test_24():
    10 in s24

s24 = Map()
for i in xrange(8000):
    s24[i]=[i]
def test_25():
    100 in s24

s25 = Map()
for i in xrange(9000):
    s25[i]=[i]
def test_26():
    1000 in s25

s26 = Map()
for i in xrange(10000):
    s26[i]=[i]
def test_27():
    10000 in s26

if __name__ == '__main__':
    print timeit.timeit('test_1()', setup="from __main__ import test_1", number=1000000)
    del s
    print timeit.timeit('test_2()', setup="from __main__ import test_2", number=1000000)
    del s1
    print timeit.timeit('test_3()', setup="from __main__ import test_3", number=100000)
    del s2
    print timeit.timeit('test_4()', setup="from __main__ import test_4", number=100000)
    del s3
    print timeit.timeit('test_5()', setup="from __main__ import test_5", number=10000)
    del s4

    print timeit.timeit('test_6()', setup="from __main__ import test_6", number=10000)
    del s5
    print timeit.timeit('test_7()', setup="from __main__ import test_7", number=10000)
    del s6
    print timeit.timeit('test_8()', setup="from __main__ import test_8", number=10000)
    del s7
    print timeit.timeit('test_9()', setup="from __main__ import test_9", number=10000)
    del s8
    print timeit.timeit('test_10()', setup="from __main__ import test_10", number=10000)
    del s9

    print ''


    print timeit.timeit('test_11()', setup="from __main__ import test_11", number=1000000)
    del s10
    print timeit.timeit('test_12()', setup="from __main__ import test_12", number=1000000)
    del s11
    print timeit.timeit('test_13()', setup="from __main__ import test_13", number=1000000)
    del s12
    print timeit.timeit('test_14()', setup="from __main__ import test_14", number=1000000)
    del s13
    print timeit.timeit('test_15()', setup="from __main__ import test_15", number=100000)
    del s14

    print ''

    print timeit.timeit('test_16()', setup="from __main__ import test_16", number=10000)
    del s15
    print timeit.timeit('test_17()', setup="from __main__ import test_17", number=10000)
    del s16
    print timeit.timeit('test_18()', setup="from __main__ import test_18", number=10000)
    del s17
    print timeit.timeit('test_19()', setup="from __main__ import test_19", number=1000000)
    del s18
    print timeit.timeit('test_20()', setup="from __main__ import test_20", number=1000000)
    del s19
    print ''

    unittest.main()
