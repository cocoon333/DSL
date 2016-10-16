from median import *

data = []
res = 0

with open('Median.txt') as f:
    for line in f:
        data.append(int(line.split("\r\n")[0]))

#r = data[:10]
#data = r

m = Median()
for element in data:
    r = m.get_median(element)
    res += r
    #print (element, r, m.hmin, m.hmax)

print res
