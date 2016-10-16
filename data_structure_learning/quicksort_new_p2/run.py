from quicksort import *
import copy

l = []
with open("_32387ba40b36359a38625cbb397eee65_QuickSort.txt") as f:
    for line in f:
        l.append(int(line.split("\r\n")[0]))

l_origin = copy.deepcopy(l)

qs = QuickSort(partition_left_pivot)
print "left pivot = ", qs.quicksort(l)
assert l ==  sorted(l)

l = copy.deepcopy(l_origin)
qs = QuickSort(partition_classic_right_pivot)
print "right pivot = ", qs.quicksort(l)
assert l ==  sorted(l)

l = copy.deepcopy(l_origin)
qs = QuickSort(partition_median_3_pivot)
print "median 3 pivot = ", qs.quicksort(l)
assert l ==  sorted(l)
