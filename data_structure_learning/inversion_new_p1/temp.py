l = []
with open("1.txt") as f:
    for line in f:
        print line.split("\r\n")
        #l.append(int(line.split("\r\n")[0])) 

print l
