from time import time


def compute_everage(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    # print(factorial(5))
    print(compute_everage(10))


if __name__ == '__main__':
    main()
