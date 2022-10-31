'''
Lambda: ham an danh
'''
# use lambda for filter function
from functools import reduce
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda n: n % 2 != 0, number_list)))
# use lambda for reduce function
sequence = [1, 3, 5, 6, 9, 2, 8]
# print(reduce(lambda a, b: a+b, sequence))
print(reduce(lambda a, b: a if a > b else b, sequence))
