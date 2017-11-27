from math import *

def factors(x):
    if x<=0:
        return 0
    i=2
    e=floor(sqrt(x))
    r=[]
    while i<=e:
        if x%i==0:
            r.append(i)
            x/=i
            e=floor(sqrt(x))
        else:
            i+=1
    if x>1: r.append(x)
    return r

def contain(lista, number):
    for x in lista:
        if x[0] == number:
            return True
    return False

def get_tuples(lista):
    result = []
    for number in lista:
        if not contain(result, number):
            result.append((number, lista.count(number)))
    return result


print get_tuples(factors(756))
