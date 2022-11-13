# R-1.1
def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False
# R-1.2


def is_even(k):
    return True if k[-1] == 0 or 2 or 4 or 6 or 8 else False


# R-1.3
def minmax(data):
    max = data[0]
    min = data[0]
    for i in range(1, len(data)):
        if data[i] > max:
            max = data[i]
        if data[i] < min:
            min = data[i]
    return max, min
# R-1.4


def sum_square(n):
    result = 0
    for i in range(1, n):
        result += i * i
    return result

# R-1.5


def sum_square_new(n):
    return sum([k*k for k in range(1, n)])
# R-1.6


def sum_square_odd(n):
    result = 0
    for i in range(1, n):
        if i % 2 != 0:
            result += i * i
    return result

# R-1.7


def sum_square_odd_new(n):
    return sum([k*k for k in range(1, n) if k % 2 != 0])


def main():
    # k = input('Please enter k:')
    # n = int(input('Please enter n:'))
    # m = int(input('Please enter m:'))
    # print(is_multiple(n, m))
    # print(is_even(list(k)))
    # print(minmax([7, 2, 5, 8, 9, 1, 5, 2, 4, 8, 11, 5]))
    # print(sum_square(5))
    # print(sum_square_new(5))
    print(sum_square_odd(5))
    print(sum_square_odd_new(5))


if __name__ == '__main__':
    main()
