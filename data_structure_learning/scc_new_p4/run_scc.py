from scc import *

data = []
for i in xrange(875714):
    data.append([])

with open("SCC.txt") as f:
    for line in f:
        line = line.split(" ")
        data[int(line[0])-1].append(int(line[1])-1)

scc = SCC()
answer = scc.scc(data)
size_of_sccs = []
for scc in answer.values():
    size_of_sccs.append(len(scc))

size_of_sccs.sort(reverse=True)
print size_of_sccs[0:5]
print len(size_of_sccs)
