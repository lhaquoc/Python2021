def vi_du(a):
    '''vi du ve dinh nghia ham'''
    print(f'Lap trinh:  {a}')


def giaiThua(n):
    giaithua = 1
    for i in range(1, n+1, 1):
        giaithua *= i
    return giaithua


def is_perfect_numer(n):
    res = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            res += i
    if n == res:
        return True
    return False


def print_perfect_number(a, b):
    for i in range(a, b):
        if is_perfect_numer(i):
            print(i)


def mahattan_distance(x, y):
    return sum(abs(val1-val2) for val1, val2 in zip(x, y))


x = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9]
y = [9.8, 8.7, 7.6, 8.5, 5.4, 4.3, 3.2, 2.1]
print(mahattan_distance(x, y))

#print_perfect_number(1, 100000)

# e_mu = 0
# x = int(input('x = '))
# for i in range(30):
#     e_mu += x**i/giaiThua(i)
# res = e_mu / (1 + e_mu)
# print(f'Sigmoid_Logistic({x}) = {res}')
# vi_du('Python')
# print(vi_du.__doc__)
