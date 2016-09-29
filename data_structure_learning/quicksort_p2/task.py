from quicksort import *
l = []
with open("QuickSort.txt") as f:
    for line in f:
        l.append(int(line.split('\r\n')[0]))

q = Quicksort()
print q.quicksort(l)
