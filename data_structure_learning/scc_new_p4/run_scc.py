from scc import *

data = []
for i in xrange(875714):
    data.append([])

with open("SCC.txt") as f:
    for line in f:
        line = line.split(" ")
        data[int(line[0])-1].append(int(line[1])-1)

scc = SCC()
print scc.scc(data)
