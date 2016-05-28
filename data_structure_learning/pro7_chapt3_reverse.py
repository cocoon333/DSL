def reverse(s):
    for i in xrange(len(s)-1):
        object = s[len(s)-1]
        s.insert(i, object)
        del s[len(s)-1]
    return s


if __name__ == '__main__':
    s = reverse([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print s
    assert(s == [9, 8, 7, 6, 5, 4, 3, 2, 1])
    s1 = reverse(input('Enter a list: '))
    print s1
    s2 = reverse(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    print s2
