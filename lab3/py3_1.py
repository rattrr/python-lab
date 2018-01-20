import math

class ComplexNumber(object):
    def __init__(self, realPart, imaginaryPart):
        self.realPart = realPart
        self.imaginaryPart = imaginaryPart
    def __str__(self):
        return "{} + {}i".format(self.realPart, self.imaginaryPart)

    def __add__(self, other):
        return ComplexNumber(self.realPart + other.realPart, self.imaginaryPart + other.imaginaryPart)

    def __sub__(self, other):
        return ComplexNumber(self.realPart - other.realPart, self.imaginaryPart - other.imaginaryPart)

    def __mul__(self, other):
        return ComplexNumber(self.realPart * other.realPart, self.imaginaryPart * other.imaginaryPart)

    def __div__(self, other):
        return ComplexNumber(self.realPart / other.realPart, self.imaginaryPart / other.imaginaryPart)

    def getMagnitude(self):
        return math.sqrt(math.pow(self.realPart, 2) + math.pow(self.imaginaryPart, 2))

    def __eq__(self, other):
        return self.getMagnitude() == other.getMagnitude()

    def __ne__(self, other):
        return self.getMagnitude() != other.getMagnitude()

    def __lt__(self, other):
        return self.getMagnitude() <  other.getMagnitude()

    def __le__(self, other):
        return self.getMagnitude() <= other.getMagnitude()

    def __gt__(self, other):
        return self.getMagnitude() >  other.getMagnitude()

    def __ge__(self, other):
        return self.getMagnitude() >= other.getMagnitude()


cn1 = ComplexNumber(10, 20)
cn2 = ComplexNumber(3, 4)

print cn1 + cn2
print cn1 - cn2
print cn1 * cn2
print cn1 / cn2

print cn1.getMagnitude()
print cn2.getMagnitude()

print cn1 > cn2
print cn1 == cn2
