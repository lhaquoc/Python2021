# -*- coding: utf-8 -*-
"""
@author: Quoc

Content: Video 4, print

"""
# cac kieu print
print()
print(5)
print("Hello Python!")
print("Chao mung ban den voi mon lap trinh Python"); print("Bai 1")
print("Xin", "Chao", "Python", 1, 2, 3, 4, sep = ",")

print('Xin chao', end=':')
print('Cac ban')

# print format
print('Ten = {0}, Ho = {1}'.format('Quoc', 'Le'))
ten = 'Hoang Anh Quoc'
ho = 'Le'
print(f'Ten = {ten}, Ho = {ho}')


def extend_list(val, list_item=[]):
    list_item.append(val)
    return list_item

def new_list(val, list_item=[]):


list1 = extend_list(5)
list2 = extend_list(555, [])
list3 = extend_list('Z')