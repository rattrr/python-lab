import sys

if sys.argv[1] != '-':
    fh = open(sys.argv[1])
    lines = fh.read().split('\n')
    fh.close()
else:
    lines = sys.stdin

for line in lines:
    if line.find(sys.argv[2]) != -1:
        print line.strip()
