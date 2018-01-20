n = [int(x) for x in raw_input("Podaj 3 liczby: ").split(" ")]
print n[0] if n[0] > n[1] and n[0] > n[2] else n[1] if n[1] > n[2] else n[2] if n[2] > n[0] else n[0]
