# -*- coding: utf-8 -*-

codes = []
for c in xrange(ord('a'), ord('z'), input("Podaj liczbę: ")):
    codes.append(c)

for i, c in enumerate(codes):
    print chr(c) if i%2==0 else chr(c-32),
