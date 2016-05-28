class Statistics(object):
    def mean(self, list):
        mean = 0
        for i in list:
            mean += i
        mean /= len(list) + 0.0
        return mean

    def median(self, list):
        list.sort()
        if len(list)%2 == 0:
            count = len(list)/2 - 1
            median = (list[count] + list[count+1]) / 2.0
        else:
            count = len(list)/2
            median = list[count]
        return median

    def mode(self, list):
        count_record = 0
        mode = 0
        for i in list:
            if list.count(i) > count_record:
                count_record = list.count(i)
                mode = i
        return mode

if __name__ == '__main__':
    S = Statistics()
    mean = S.mean([1, 2, 3, 4, 5, 6, 7, 8, 9])
    median1 = S.median([5, 4, 6, 3, 7, 2, 8, 1, 9, 10])
    median2 = S.median([5, 4, 6, 3, 7, 2, 8, 1, 9])
    mode = S.mode([1, 1, 2, 4, 4, 7, 7, 7, 7])

    assert(mean == 5.0)
    assert(median1 == 5.5)
    assert(median2 == 5)
    assert(mode == 7)

    print 'The program is running smoothly'


#DONE
