#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Sat Apr  9 22:11:33 2022

@author: anhquoc
'''

a = input('Nhap vao so a: ')
print('Kieu du lieu cua a: ', type(a))
a = float(a)
print('Kieu du lieu cua a: ', type(a))

b = input('Nhap vao so b: ')
print('Kieu du lieu cua b: ', type(b))
b = float(b)
print('Kieu du lieu cua a: ', type(b))

print('{0} + {1} = {2}'.format(a, b, a + b))
print('{0} - {1} = {2}'.format(a, b, a - b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print('{0} / {1} = {2}'.format(a, b, a / b))
print('{0} ** {1} = {2}'.format(a, b, a ** b))
print('{0} % {1} = {2}'.format(a, b, a % b))
print('{0} // {1} = {2}'.format(a, b, a // b))