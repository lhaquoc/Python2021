import sys
import stdio

a = int(sys.argv[0])
b = int(sys.argv[1])

total = a + b
diff = a - b
prod = a * b
quot = a // b
rem = a % b
exp = a ** b

stdio.writeln(str(a) + ' + ' str(b) + ' = ' + str(total))
