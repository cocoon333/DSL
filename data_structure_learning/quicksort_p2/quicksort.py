class Quicksort(object):
    def __init__(self):
        self.comparsions = 0

    def quicksort(self, v):
        self.comparsions = 0
        self.quicksort_helper(v, 0, len(v)-1)
        return self.comparsions

    def quicksort_helper(self, v, l, h):
        assert(l <= h)
        assert(type(v) == list)
        assert(l < len(v) and l >= 0)
        assert(h >= 0 and h < len(v))
        if len(v) > 1:
            pivot_index = self.partition(v, l, h)
            if pivot_index != l:
                self.quicksort_helper(v, l, pivot_index-1)
            if pivot_index != h:
                self.quicksort_helper(v, pivot_index+1, h)

    def partition(self, v, l, h):
        assert(l <= h)
        assert(type(v) == list)
        assert(l < len(v) and l >= 0)
        assert(h >= 0 and h < len(v))
        pivot = v[l]
        #pivot = v[h]
        self.comparsions += h - l
        i = l
        for j in xrange(l+1, h+1):
            if v[j] < pivot:
                a = v[i+1]
                v[i+1] = v[j]
                v[j] = a
                i += 1
        v[l] = v[i]
        v[i] = pivot
        assert(i >= l and i <= h)
        return i
       #for j in xrange(l+1, h+1):
       #    if v[j] < pivot:
       #        a = v[i+1]
       #        v[i+1] = v[j]
       #        v[j] = a
       #        i += 1
       #res = 0
       #if v[l] > pivot:
       #    a = v[l]
       #    v[l] = pivot
       #    v[h] = a
       #    a = v[i]
       #    v[i] = pivot
       #    v[l] = a
       #    res = i
       #else:
       #    v[h] = v[i+1]
       #    v[i+1] = pivot
       #    res = i+1
       #assert(i >= l and i <= h)
       # return res
