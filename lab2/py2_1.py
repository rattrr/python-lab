def lens(str):
    return [(word, len(word)) for word in str.split()]

print lens("d dd ddd dddd5")
