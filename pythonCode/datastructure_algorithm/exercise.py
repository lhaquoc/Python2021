# 1.12
# R-1.1
def is_multiple(n, m):
    try:
        return True if (int(n) % int(m) == 0) else False
    except ValueError as error:
        print(f'Error! {error}. Numbers must be Integer values.')


# R-1.2
def is_even(k):
    try:
        # return int(k) & 1 == 0
        return int(k) % 2 == 0
    except ValueError as error:
        print(f'Error! {error}. Numbers must be Integer values.')


# R-1.3
def minmax(data):
    min_element = data[0]
    max_element = data[0]
    for i in range(1, len(data)):
        if data[i] < min_element:
            min_element = data[i]
        if data[i] > max_element:
            max_element = data[i]
    return min_element, max_element


# R-1.4
def sum_of_squares(n):
    sum = 0
    for i in range(n):
        sum += i * i
    return sum


# R-1.5
def sum_of_squares_compre(n):
    return sum([x * x for x in range(n) if x < n])


# R-1.6
def sum_of_squares_odd(n):
    sum = 0
    for i in range(n):
        if i % 2 != 0:
            sum += i * i
    return sum


# R-1.7
def sum_of_squares_odd_compre(n):
    return sum([x * x for x in range(n) if x < n and x % 2 != 0])


print(is_multiple(30, 3))
print(is_even(4))
print(minmax([1, 2, 3, 4, 5, 9, 0, 21, -5, -2, -1, -6, 11]))
print(sum_of_squares(10))
print(sum_of_squares_compre(10))
print(sum_of_squares_odd(10))
print(sum_of_squares_odd_compre(10))
