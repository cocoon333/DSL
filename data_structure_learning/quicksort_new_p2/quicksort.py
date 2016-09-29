class QuickSort(object):
    def __init__(self):
        self.res = 0

    def quicksort(self, data):
        assert data
        self.res = 0
        self.quicksort_rec(data, 0, len(data)-1)
        return self.res

    def quicksort_rec(self, data, l, r):
        assert l <= r
        if l == r:
            return
        self.res += r - l
        pivot = self.partition(data, l, r)
        self.quicksort_rec(data, l, pivot)
        if pivot < r:
            self.quicksort_rec(data, pivot+1, r)

    def partition(self, data, l, r):
        assert l <= r
        if l+1 == r:
            if data[l] > data[r]:
                self.swap(data, l, r)
                return r
            else:
                assert(data[l] <= data[r])
                return l

        i = l + 1
        j = r
        while (i != r or j != r) and j >= i:
            while i < r and data[i] <= data[l]:
                i += 1
            
            while j > 0 and data[j] > data[l]:
                j -= 1

            if i < j:
                self.swap(data, i, j)

        self.swap(data, j, l)
        return j

    def swap(self, data, i, j):
        k = data[i]
        data[i] = data[j]
        data[j] = k
