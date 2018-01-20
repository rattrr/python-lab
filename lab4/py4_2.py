import sys

def str_to_dict(str):
    lines = str.split('\n')
    dct = dict()
    for line in lines:
        line = line.split(': ')
        if len(line) > 1:
            dct[line[0]] = line[1]
    return dct

with open(sys.argv[1]) as f:
    print str_to_dict(f.read())
