'''
Iterables and Iterators

iterable: types of iterables
list/tuple/str/dict
zip/enumerate/range/reversed
iterator: An iterable can be passed to the built-in function iter(), which returns some object called iterator

'''
it = iter([4, 3, 2, 1])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
