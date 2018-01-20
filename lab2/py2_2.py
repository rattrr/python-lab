def fibo_gen():
    previous, current = 0, 1
    while True:
        yield current
        previous, current = current, previous + current


n = input("n: ")
gen = fibo_gen()
print [gen.next() for x in xrange(n)]
