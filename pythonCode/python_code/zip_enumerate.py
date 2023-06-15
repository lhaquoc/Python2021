'''
Zip and Enumerate

zip(): to zip 2 lists together
enumerate(): to return both item & index corresponding to that item in the list
'''

intergers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped = zip(intergers, letters, floats)
print(zipped)
print(list(zipped))

my_list = ['h', 'e', 'l', 'l', 'o']
for idx, item in enumerate(my_list):
    print(idx, item)
