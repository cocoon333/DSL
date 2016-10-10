from dijkstra import *

data = []

with open("dijkstraData.txt") as f:
    for line in f:
        node = []
        line = line.split('\t')
        for i in line[1:len(line)-1]:
            i = i.split(',')
            node.append(int(i[0])-1)
            node.append(int(i[1]))
        data.append(node)

d = Dijkstra()
raw_res = d.dijkstra(data)
res = []

for i in [7,37,59,82,99,115,133,165,188,197]:
    res.append(str(raw_res[i-1]))

s = ",".join(res)
print s
