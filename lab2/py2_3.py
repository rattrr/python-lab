def filter(condition, list):
    return [x for x in list if condition(x)]

print filter(lambda x: x>15, [4, 8, 15, 16, 32, 42])
