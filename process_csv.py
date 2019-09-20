import sys
f = open(sys.argv[1], 'r')

out = open("out.txt", 'w')

header = f.readline().split(',')
header = ['#HOT'] + ['s' + str(int(s)+1)+'r1' for s in header[1:]]
header = "\t".join(header)
out.write(header +'\n')

for line in f:
    while ',,' in line:
        line = line.replace(',,', ',na,')
    line = line.split(',')
    line = "\t".join(line)
    out.write(line +'\n')

out.close()
