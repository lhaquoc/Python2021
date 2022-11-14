# Functions Can Return Something
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d x %d" % (a, b))
    return a * b


def divide(a, b):
    print("DEVIDING %d : %d" % (a, b))
    return a / b


def main():
    print("Let's do some math with just functions!")
    age = add(30, 5)
    height = subtract(78, 4)
    weight = multiply(90, 2)
    iq = divide(100, 2)
    print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

    print("Here is a puzzle.")
    what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
    print("That becomes: ", what, "Can you to do it by hand?")


if __name__ == '__main__':
    main()
