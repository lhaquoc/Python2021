# for element in iterable
data = [1, 2, 3, 4]

i = iter(data)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

for j in i:
    print(j)

for element in data:
    print(element)


# generators
def factors(n):
    for k in range(1, n + 1):
        if n % k == 0:
            yield k


def first(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

# f = factors(3)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

# sum_of_first_n = sum(first(1000000))
sum_of_first_n = sum(firstn(1000000))

