def get_pivot_for_median_3(data, l, r):
    assert (r > l)
    if l + 1 == r:
        return l
    m = l+(r-l)/2
    med = 0
    if data[l] >= data[m]:
        if data[m] >= data[r]:
            med = m
        elif data[l] >= data[r]:
            med = r
        else:
            med = l
    else:
        if data[m] <= data[r]:
            med = m
        elif data[r] >= data[l]:
            med = r
        else:
            med = l
    assert (data[med]  == sorted([data[l], data[m], data[r]])[1])
    return med

def partition_median_3_pivot(data, l, r):
    assert l <= r
    med = get_pivot_for_median_3(data, l, r)
    swap(data, l, med)
    return partition_left_pivot(data, l, r)

def partition_right_pivot(data, l, r):
    assert l <= r
    i = l
    for j in xrange(l, r):
        if data[j] < data[r]:
            swap(data, j, i)
            i += 1
    swap(data, r, i)
    return i

def partition_classic_right_pivot(data, l, r):
    swap(data, l, r)
    return partition_left_pivot(data, l, r)


def partition_left_pivot(data, l, r):
    assert l <= r
    i = l+1
    for j in xrange(l+1,r+1):
        if data[j] < data[l]:
            swap(data, j, i)
            i += 1
    swap(data, l, i-1)
    return i-1

def partition_left_right(data, l, r):
    assert l <= r
    if l+1 == r:
        if data[l] > data[r]:
            swap(data, l, r)
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
            swap(data, i, j)

    swap(data, j, l)
    return j

def swap(data, i, j):
    k = data[i]
    data[i] = data[j]
    data[j] = k

class QuickSort(object):
    def __init__(self, partition_method=partition_left_right):
        self.res = 0
        self.partition_method = partition_method

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
        pivot = self.partition_method(data, l, r)
        if pivot > l:
            self.quicksort_rec(data, l, pivot-1)
        if pivot < r:
            self.quicksort_rec(data, pivot+1, r)

