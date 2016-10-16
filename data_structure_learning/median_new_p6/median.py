import heapq

class Median(object):
    def __init__(self):
        self.median = 0 
        self.hmin = []
        self.hmax = []

    def get_median(self, n):
        if len(self.hmin) == len(self.hmax):
            if n <= self.median:
                heapq.heappush(self.hmin, n)
                self.median = heapq.nlargest(1, self.hmin)[0]
            else:
                assert (n > self.median)
                heapq.heappush(self.hmax, n)
                self.median = heapq.nsmallest(1, self.hmax)[0]

        elif len(self.hmin) < len(self.hmax):
            if n <= self.median:
                heapq.heappush(self.hmin, n)
                self.median = heapq.nlargest(1, self.hmin)[0]
            else:
                assert (n > self.median)
                item = heapq.heappop(self.hmax)
                heapq.heappush(self.hmin, item)
                heapq.heappush(self.hmax, n)
                self.median = heapq.nlargest(1, self.hmin)[0]

        else: 
            assert (len(self.hmin) > len(self.hmax))
            if n <= self.median:
                item = self._heappop_max(self.hmin)
                heapq.heappush(self.hmax, item)
                heapq.heappush(self.hmin, n)
                self.median = heapq.nlargest(1, self.hmin)[0]
            else:
                assert (n > self.median)
                heapq.heappush(self.hmax, n)
                self.median = heapq.nlargest(1, self.hmin)[0]
        return self.median

    def _heappop_max(self, heap):
        """Maxheap version of a heappop."""
        heapq._heapify_max(heap)
        res = heapq.heappop(heap)
        heapq.heapify(heap)
        return res
