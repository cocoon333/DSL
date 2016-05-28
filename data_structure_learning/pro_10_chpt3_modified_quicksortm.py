#import random
#import time
def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst)-1)

def quicksortHelper(lyst, left, right):
    if len(lyst) <= 200:
        return selectionSort(lyst)
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
    middle = (left+right)/2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    boundary = left
    for index in range(left, right):
        if lyst[index] < pivot:
            a = lyst[index]
            lyst[index] = boundary
            lyst[boundary] = a
            boundary += 1
    a = lyst[right]
    lyst[right] = boundary
    lyst[boundary] = a
    return boundary

def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            a = lyst[i]
            lyst[i] = lyst[minIndex]
            lyst[minIndex] = a
        i += 1
"""
if __name__ == '__main__':
    l = []
    for i in xrange(50):
        j = random.randint(1, 20)
        l.append(j)
    begin = time.time()
    quicksort(l)
    total_time = time.time() - begin
    print total_time

    l = []
    for i in xrange(500):
        j = random.randint(1, 20)
        l.append(j)
    begin = time.time()
    quicksort(l)
    total_time = time.time() - begin
    print total_time

    l = []
    for i in xrange(5000):
        j = random.randint(1, 20)
        l.append(j)
    begin = time.time()
    quicksort(l)
    total_time = time.time() - begin
    print total_time
"""
