# -*- coding: utf-8 -*-
from string import ascii_lowercase, maketrans


def caesar(text, shift):
    before_shift = ascii_lowercase
    after_shift = before_shift[shift:] + before_shift[:shift]
    translation_table = maketrans(before_shift, after_shift)
    return text.translate(translation_table)

text = raw_input("Tekst do zaszyfrowania: ")
shift = input("Przesunięcie: ")

print("Wynik: " + caesar(text, shift))
