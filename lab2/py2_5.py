# -*- coding: utf-8 -*-
import os, sys

def generator(path, extension):
    for filename in os.listdir(path):
        if filename.endswith(extension):
            yield filename


gen = generator(sys.argv[1], sys.argv[2])

decision = True;
while decision:
    try:
        print gen.next()
        decision = True if raw_input("wypisać kolejny plik? [y/n]  ").lower() == "y" else False
    except StopIteration:
        print "Nie ma więcej plików"
        break
