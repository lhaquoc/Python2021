import Stack
import Inversed_Stack

'''
  stack
'''
s = Stack.Stack()
print(s.is_empty())
s.push(4)
s.push('dog')
print(s.items)
s.push('a')
s.push(True)
print(s.items[::-1])

'''
  inversed stack
'''
i_s = Inversed_Stack.Inversed_Stack()
print(i_s.is_empty())
i_s.push(1)
i_s.push('myName')
i_s.push(False)
print(i_s.items)
print(i_s.peek())
print(i_s.pop())  # changed the stack
print(i_s.items)

s2 = Stack.Stack()
s2.push('x')
s2.push('y')
s2.push('z')
while not s2.is_empty():
    s2.pop()
    s2.pop()
