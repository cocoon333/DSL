from inversion import *
l = []
with open("_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt") as f:
    for line in f:
       l.append(int(line.split("\r\n")[0])) 

i = Inversion(merge_method=merge_new)
print i.calculate(l)
