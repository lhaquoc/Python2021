from time import time
import dynamic_array


def compute_everage(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n


def main():
    print(compute_everage(10))


if __name__ == '__main__':
    main()
