def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return recur_factorial(n - 1) * n

def permute(string, pocket = ""):
    if (len(string) == 0):
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)

print(iterative_factorial(5))
print(recur_factorial(5))
print(permute("abcd", ""))
