'''
a =  [1, 5, 3, -1, -2, 9, 5, 6]
1. tim so nho nhat trong a
2. tim so lon nhat trong a

min = a[0]
a[1] so sanh voi min, se co 2 truong hop
- a[1] > min: min k doi
- a[1] <= min: min = a[1]
lap lai, a[2] so sanh voi min
- a[2] > min: min k doi
- a[2] <= min: min = a[2]
'''
a =  [1, 5, 3, -1, -2, 9, 5, 6, -3]

def find_min(a):
    min_item = a[0]
    for i in range(1, len(a)):
        if a[i] <= min_item:
            min_item = a[i]
    print(min_item)

find_min(a)
print(min(a))
print(max(a))
