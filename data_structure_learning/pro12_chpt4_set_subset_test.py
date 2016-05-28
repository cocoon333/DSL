def isSubsetOf(setA, setB):
    for element in setA:
        if element not in setB:
            return False
    return True

if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert(isSubsetOf(l1, l2))
    l1 = [6, 5, 3, 7, 346, 5, 7, 4, 56, 34, 5, 43, 6, 45, 7, 45, 2, 4326, 5, 3, 4, 5, 32]
    l2 = [4, 33, 5]
    assert(not isSubsetOf(l1, l2))
    l1 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    l2 = [1, 2, 3, 4, 5, 6]
    assert(isSubsetOf(l1, l2))
    print 'All tests are passed!'
