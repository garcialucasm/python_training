def c_half(n=0):
    n = n*0.5
    return n


def c_double(n=0):
    n = n*2
    return n


def increase_10(n=0, tax=0):
    n = n + n*tax/100
    return n


def decrease_11(n=0, tax=0):
    n = n - n*tax/100
    return n


def c_format(n=0):
    return f'${n:.2f}'.replace('.', ',')