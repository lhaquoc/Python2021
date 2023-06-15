'''
Lambda Expressions

Syntax: lambda argument_list: expression
argument_list (same as argument list in functions): x,y, *arg, **kwargs
expression (Output) must be single line
'''

mul = lambda x, y: x*y
lambda *args: sum(args)
lambda x: 1

print(mul(5, 6))

# sorted
print(sorted([1, 2, 3, 4, 5], key = lambda x: abs(3 - x)))
# filter and map
print(list(filter(lambda n: n % 2 == 1, [1, 2, 3, 4, 5])))
print(list(map(lambda x: x + 1, [1, 2, 3])))
