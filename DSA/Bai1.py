import random as rd


def turns(n, low, high):
    turns = 0
    while high >= low:
        turns += 1
        mid = (low + high) / 2
        if mid == n:
            return turns
        elif mid < n:
            low = mid + 1
        else:
            high = mid - 1
    return turns


def search(A, t):
    for i in range(0, len(A)):
        if A[i] == t:
            return True
    return False

# insert sort


def insert(A, pos, value):
    i = pos - 1
    while i >= 0 and A[i] > value:
        A[i+1] = A[i]
        i -= 1
    A[i+1] = value


def insertSort(A):
    for pos in range(1, len(A)):
        insert(A, pos, A[pos])
# selection sort


def main():
    # print(turns(5, 2, 9))
    A = [1, 4, 8, 9, 11, 15, 17, 22, 23, 26]
    B = []
    for i in range(1, 1000):
        B.append(rd.randint(0, 1000))
    print(B)
    print(search(A, 15))
    insertSort(B)
    print(B)


if __name__ == '__main__':
    main()
