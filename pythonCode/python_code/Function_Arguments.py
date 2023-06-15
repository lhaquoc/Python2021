# required and default parameters

def print_name(name, greeting='Welcome cac ban'):
    print(f'{name}, {greeting}')
# variable-length params (*args, **kwargs)


def variableLengthArgExample(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)


def myFunc(a, b, c):
    print(a, b, c)


def main():
    print_name('Quoc', 'bye cac ban')
    myFunc(1, 2, 3)
    # keyword arguments
    myFunc(a='Hello word!', c='C value', b=2)
    variableLengthArgExample('a', 'b', 'Hello', 1, 2, size='Up size', age='NG')


if __name__ == '__main__':
    main()
