import timeit
class Set():
    def __init__(self):
        self.set = []

    def __len__(self):
        return len(self.set)

    def __contains__(self, item):
        if item in self.set:
            return True
        return False

    def add(self, item):
        if item not in self.set:
            self.set.append(item)

    def remove(self, element):
        try:
            self.set.remove(element)
        except:
            raise AssertionError

    def __eq__(self, other):
        if len(self.set) == len(other):
            if self.__lt__(other):
                return True
        return False

    def __lt__(self, other):
        for element in self.set:
            if element not in other:
                return False
        return True

    def __add__(self, other):
        union_set = Set()
        for element in self.set:
            union_set.add(element)
        for element in other.set:
            union_set.add(element)
        return union_set

    def __mul__(self, other):
        intersect_set = Set()
        for element in self.set:
            if element in other:
                intersect_set.add(element)
        return intersect_set

    def __sub__(self, other):
        difference_set = Set()
        for element in self.set:
            if element not in other:
                difference_set.add(element)
        return difference_set

    def forward(self, element):
        index = self.set.index(element)
        if index >= 0:
            if index != 0:
                return self.set[index-1]
        return None

    def backward(self, element):
        index = self.set.index(element)
        if index >= 0:
            if index != len(self.set)-1:
                return self.set[index+1]
        return None


    def __str__(self):
        return str(self.set)

    def __repr__(self):
        return self.__str__()


s = Set()
s.add(1)
def test_1():
    len(s)

s1 = Set()
for i in xrange(10):
    s1.add(i)
def test_2():
    len(s1)

s2 = Set()
for i in xrange(100):
    s2.add(i)
def test_3():
    len(s2)

s3 = Set()
for i in xrange(1000):
    s3.add(i)
def test_4():
    len(s3)

s4 = Set()
for i in xrange(10000):
    s4.add(i)
def test_5():
    len(s4)

#---------------------------------------------------------------------------------------------------

s5 = set()
s5.add(1)
def test_6():
    len(s5)

s6 = set()
for i in xrange(10):
    s6.add(i)
def test_7():
    len(s6)

s7 = set()
for i in xrange(100):
    s7.add(i)
def test_8():
    len(s7)

s8 = set()
for i in xrange(1000):
    s8.add(i)
def test_9():
    len(s8)

s9 = set()
for i in xrange(10000):
    s9.add(i)
def test_10():
    len(s9)


#===================================================================================================


s10 = Set()
s.add(10)
def test_11():
    1 in s10

s11 = Set()
for i in xrange(10):
    s11.add(i)
def test_12():
    10 in s13

s12 = Set()
for i in xrange(100):
    s12.add(i)
def test_13():
    100 in s12

s13 = Set()
for i in xrange(1000):
    s13.add(i)
def test_14():
    1000 in s13

s14 = Set()
for i in xrange(10000):
    s14.add(i)
def test_15():
    10000 in s14

#---------------------------------------------------------------------------------------------------

s15 = set()
s15.add(1)
def test_16():
    2 in s15

s16 = set()
for i in xrange(10):
    s16.add(i)
def test_17():
    10 in s16

s17 = set()
for i in xrange(100):
    s17.add(i)
def test_18():
    100 in s17

s18 = set()
for i in xrange(1000):
    s18.add(i)
def test_19():
    1000 in s18

s19 = set()
for i in xrange(10000):
    s19.add(i)
def test_20():
    10000 in s19


if __name__ == '__main__':
    print timeit.timeit('test_1()', setup="from __main__ import test_1", number=10000000)
    del s
    print timeit.timeit('test_2()', setup="from __main__ import test_2", number=10000000)
    del s1
    print timeit.timeit('test_3()', setup="from __main__ import test_3", number=10000000)
    del s2
    print timeit.timeit('test_4()', setup="from __main__ import test_4", number=10000000)
    del s3
    print timeit.timeit('test_5()', setup="from __main__ import test_5", number=10000000)
    del s4
    print ''

    print timeit.timeit('test_6()', setup="from __main__ import test_6", number=10000000)
    del s5
    print timeit.timeit('test_7()', setup="from __main__ import test_7", number=10000000)
    del s6
    print timeit.timeit('test_8()', setup="from __main__ import test_8", number=10000000)
    del s7
    print timeit.timeit('test_9()', setup="from __main__ import test_9", number=10000000)
    del s8
    print timeit.timeit('test_10()', setup="from __main__ import test_10", number=10000000)
    del s9
    print '\n'


    print timeit.timeit('test_11()', setup="from __main__ import test_11", number=10000000)
    del s10
    print timeit.timeit('test_12()', setup="from __main__ import test_12", number=10000000)
    del s11
    print timeit.timeit('test_13()', setup="from __main__ import test_13", number=1000000)
    del s12
    print timeit.timeit('test_14()', setup="from __main__ import test_14", number=100000)
    del s13
    print timeit.timeit('test_15()', setup="from __main__ import test_15", number=10000)
    del s14
    print ''

    print timeit.timeit('test_16()', setup="from __main__ import test_16", number=10000000)
    del s15
    print timeit.timeit('test_17()', setup="from __main__ import test_17", number=10000000)
    del s16
    print timeit.timeit('test_18()', setup="from __main__ import test_18", number=10000000)
    del s17
    print timeit.timeit('test_19()', setup="from __main__ import test_19", number=10000000)
    del s18
    print timeit.timeit('test_20()', setup="from __main__ import test_20", number=10000000)
    del s19
    print '\n'
