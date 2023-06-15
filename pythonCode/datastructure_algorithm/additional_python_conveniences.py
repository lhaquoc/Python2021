# conditional expressions
# expr1 if condition else expr2
n = 5
# type 1:
if n > 0:
    param = n
else:
    param = -n
# type 2:
param = n if n > 0 else -n

print(param)

# Comprehension
# type 1:
# [ expression for value in iterable if condition ]

# type 2:
# result = []
# for value in iterable:
#     if condition:
#         result.append(expression)

# type 2
squares = []
for k in range(1, n + 1):
    squares.append(k * k)

print(squares)

# type 1
squares = [k * k for k in range(1, n + 1)]
print(squares)
# set
squares = {k * k for k in range(1, n + 1)}
print(squares)
# generator
squares = (k * k for k in range(1, n + 1))
print(list(squares))
# dictionary
squares = {k: k * k for k in range(1, n + 1)}
print(squares)
