import sys
import textwrap

inputfile = sys.argv[1]
width = sys.argv[2]

with open(inputfile, 'r') as f:
	from_file = f.read().replace('\n', ' ')

print "\n".join(textwrap.wrap(from_file, int(width)))


