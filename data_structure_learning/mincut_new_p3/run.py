from mincut import *

l = {}

with open("kargerMinCut.txt") as f:
    for line in f:
        line = line.split("\t")
        l[line[0]] = line[1:len(line)-1]

mc = MinCut()
print mc.mincut(l)
