from string import ascii_lowercase, maketrans
import sys

def caesar(text, shift):
    before_shift = ascii_lowercase
    after_shift = before_shift[shift:] + before_shift[:shift]
    translation_table = maketrans(before_shift, after_shift)
    return text.translate(translation_table)




with open(sys.argv[1], "r") as inputf, open(sys.argv[2], "w") as outputf:
    outputf.write(caesar(inputf.read(), 3))
