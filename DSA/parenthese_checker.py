import Stack


def par_checker(symbol_string):
    s = Stack.Stack()
    balanced = True
    index = 0
    l = len(symbol_string)
    while index < l and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False


print(par_checker('((()))'))
print(par_checker('((()'))
