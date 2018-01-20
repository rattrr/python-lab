import math

class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Point2D({}, {})".format(self.x, self.y)
    def distanceTo(self, other):
        return math.sqrt(math.pow((self.x - other.x), 2) + math.pow((self.y - other.y), 2))


class Point3D(Point2D):
    def __init__(self, x, y, z):
        Point2D.__init__(self, x, y)
        self.z = z
    def __repr__(self):
		return "Point3D({}, {}, {})".format(self.x, self.y, self.z)
    def distanceTo(self, other):
        return math.sqrt(math.pow((self.x - other.x), 2) + math.pow((self.y - other.y), 2) + math.pow((self.z - other.z), 2))

p1 = Point2D(0, 0)
p2 = Point2D(2, 5)

p3 = Point3D(1, 2, 3)
p4 = Point3D(10, 20, 30)

print p1, p2, p3, p4
print p1.distanceTo(p2)
print p3.distanceTo(p4)
