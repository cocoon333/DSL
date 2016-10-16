def has_2_sum(data, t):
    for i in data:
        if t-i in data:
            return True
    return False


def run_2_sum(fn):
    d = []
    with open(fn, 'r') as f:
        for l in f:
            #data.add(int(l.split('\r\n')[0]))
            d.append(int(l.split('\r\n')[0]))
    data = set(d)
    sum = 0
    for t in xrange(-10000, 10000+1):
        if has_2_sum(data, t):
            sum += 1
    return sum


if __name__ == "__main__":
    res = run_2_sum('algo1-programming_prob-2sum.txt')
    #res = run_2_sum('test_2_sum.txt')
    print res


