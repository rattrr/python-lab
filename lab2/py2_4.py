import math

def calculate_and_sort_distances(list, point_as_tuple):
    nl = [(math.hypot(x - point_as_tuple[0], y - point_as_tuple[1]), "punkt({}, {})".format(x, y)) for x, y in list]
    return sorted(nl, key = lambda x: x[0])

l = [(1.5, 1.9), (8.0, 9.0), (20.3, 3.1), (2.0, 1.1), (1.0, 0.4), (0.1, 0.1)]

for point_distance in calculate_and_sort_distances(l, (20, 2)):
    print point_distance
