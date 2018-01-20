# -*- coding: utf-8 -*-

numbers = [int(x) for x in raw_input("Podaj liczby do sortowania oddzielone spacjami: ").split(" ")]

def get_and_format_range():
    range_str = raw_input("Podaj zakres liczb (n:m, n: lub :m) ")
    if(len(range_str) == 2 and range_str.startswith(':')):
        range_str = "0" + range_str
    elif(len(range_str) == 2 and range_str.endswith(':')):
        range_str = range_str + str(len(numbers))
    return [int(x) for x in range_str.split(":")]


sort_order = raw_input("Podaj kierunek sortowania (ASC / DESC): ")
if(sort_order == "ASC"):
    numbers.sort()
elif(sort_order == "DESC"):
    numbers.sort(reverse = True)
else:
    print "Nieprawidłowy kierunek sortowania"


ranges =  get_and_format_range()
print(numbers[ranges[0]:ranges[1]])
