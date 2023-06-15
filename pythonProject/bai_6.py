def function19():
    for i in range(3, 20, 3):
        print(i)


function19()
# range(start, stop, steps): số bắt đầu, kết thúc, và bước nhảy
# range(1, 10, 2): 1, 3, 5, 7, 9
print([i for i in range(10)])
print(range(10, 20))
print(range(10, 20, 2))

# newlist = [expression for item in iterable if condition == True]
newList = [x % 5 for x in range(100) if x % 6 == 0]
print(newList)

myList = []
for x in range(100):
    if x % 5 == 0:
        myList.append(x % 2)
print(myList)

