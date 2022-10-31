my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(f'{key}: {value}')

# while <condition: boolean>:
# action
# if <condition: boolean> break
# if <condition: boolean> continue
msg = ''
while msg != 'quit':
    msg = input('Please enter your name:')
    print(msg)
