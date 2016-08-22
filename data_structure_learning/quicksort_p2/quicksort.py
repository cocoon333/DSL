class Quicksort(object):
    def quicksort(self, l):
        self.l = l
        self.comparsions = 0
        self.quicksort_helper(l)
        return l

    def quicksort_helper(self, l):
        if len(l) <= 1:
            return 1
        pivot = l[0]
        self.partition(l, pivot)
        self.quicksort_helper(l[:l.index(pivot)+1])
        self.quicksort_helper(l[l.index(pivot)+1:])

    def partition(self, l, pivot):
        pivot_index = self.l.index(pivot)
        self.comparsions += len(l) - 1
        i = 0
        for j in xrange(len(l)):
            if l[j] < pivot:
                a = l[i+1]
                self.l[pivot_index+i+1] = l[j]
                self.l[pivot_index+j] = a
                i += 1
        self.l[pivot_index] = l[i]
        self.l[pivot_index+i] = pivot
