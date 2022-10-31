#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 22:33:48 2022

@author: anhquoc
"""

print('Vi du ve toan tu so sanh:\n')
a = int(input('Nhap so a:'))
b = int(input('Nhap so b:'))

# true or false
print('{0} < {1} : {2}'.format(a, b, a < b))
print('{0} > {1} : {2}'.format(a, b, a > b))
print('{0} == {1} : {2}'.format(a, b, a == b))
print('{0} != {1} : {2}'.format(a, b, a != b))
print('{0} <= {1} : {2}'.format(a, b, a <= b))
print('{0} >= {1} : {2}'.format(a, b, a >= b))

print('Vi du ve phep toan logic')
c = int(input('Nhap so c:'))
print('{0} < {1} and {2} < {3} = {4}'.format(a, b, b, c, (a < b) and (b < c)))
print('{0} < {1} or {2} < {3} = {4}'.format(a, b, b, c, (a < b) or (b < c)))
print('not ({0} > {1}) = {2}'.format(a, b, not(a > b)))