def str_to_dict(str):
    lines = str.split('\n')
    dct = dict()
    for line in lines:
        line = line.split(': ')
        dct[line[0]] = line[1]
    return dct

str = '''k1: v1
asdf: ghjk
zzzzz: xx'''

print str_to_dict(str)
