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
        return int(k) & 1 == 0
    except ValueError as error:
        print(f'Error! {error}. Numbers must be Integer values.')




print(is_multiple(30, 3))
print(is_even(4))
