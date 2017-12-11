def num2text(n):
    if n < 0 or n > 3:
        raise ValueError
    return {
        0: 'zero',
        1: 'jeden',
        2: 'dwa',
        3: 'trzy',
    }.get(n)
