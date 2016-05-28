def selectionSort(lyst, reverse=False):
    if reverse == False:
        for i in xrange(len(lyst)-1):
            minItem = min(lyst[i:])
            index = lyst.index(minItem)

            if index != i:
                lyst[index] = lyst[i]
                lyst[i] = minItem

    else:
        for i in xrange(len(lyst)-1):
            maxItem = max(lyst[i:])
            index = lyst.index(maxItem)

            if index != i:
                lyst[index] = lyst[i]
                lyst[i] = maxItem

    return lyst
"""
if __name__ == '__main__':
    l = selectionSort([5, 2, 9, 8, 1, 3, 7, 4, 0, 6])
    assert(l == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    l = selectionSort([5, 2, 9, 8, 1, 3, 7, 4, 0, 6], reverse = True)
    assert(l == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    l = selectionSort(input('Enter a list of numbers: '))
    print l
"""
