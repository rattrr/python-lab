import sys
import textwrap

inputfile = sys.argv[1]
width = int(sys.argv[2])

with open(inputfile, 'r') as f:
	from_file = f.read().replace('\n', ' ')

wrapped = textwrap.wrap(from_file, width)

for line in wrapped:
	print line.center(width)
