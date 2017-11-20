import math

def sqrt():
    number = input()
    return math.sqrt(number)


try:
    print sqrt()
except ValueError as err:
    print err
    print "Negative number"
except NameError as err:
    print err
    print "Not a number"
except SyntaxError as err:
    print err
    print "Something else"
