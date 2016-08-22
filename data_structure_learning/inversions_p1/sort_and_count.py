class SortAndCount(object):
    def __init__(self):
        self.inversions = 0

    def merge_sort(self, l):
        if len(l) <= 1:
            return l
        else:
            ll = l[0:middle]
            lr = l[middle:]
            middle = len(l)/2
            ll = self.merge_sort(ll)
            lr = self.merge_sort(lr)
            return self.merge(ll, lr)

    def merge(self, ll, lr):
        i = 0
        j = 0
        res = []
        for i in xrange(len(ll)+len(lr))
            if ll[i] <= lr[j]:
                res.append(ll[i])
                i += 1

            else:
                assert(ll[i] > lr[j])
                res.append(lr[j])
                inversions += 1
                j += 1
        assert(len(res) == len(ll) + len(lr))
        return res
