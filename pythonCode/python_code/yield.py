def gen():
    for value in range(3):
        print('yield', value + 1, 'times')
        yield value


for value in gen():
    print(value)
