# -*- coding: utf-8 -*-


def print_fibo_sequence(n):
    previous, current = 0, 1
    while current < n:
        print current,
        previous, current = current, previous + current

print_fibo_sequence(input("Podaj zakres dla ciągu Fibonacciego: "))
