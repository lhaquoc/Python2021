from pygears import gear


@gear
def filter(x, b0, b1, b2):
    x1 = mac(x, b0)
    x2 = mac(x1, b1)
    return x2 * b2


@gear
def add(a, b):
    return a + b
