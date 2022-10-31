#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 23:21:03 2022

@author: anhquoc
"""

x = input('Nhap vao x:')
x = int(x)

if x > 0:
    print(x, 'la so nguyen duong')
    
if x % 2 == 0:
    print(x, 'la so chan')
else:
    print(x, "la so le")

if x >= 9:
    print('Xuat sac')
elif x >= 8:
    print('Gioi')
elif x >= 7:
    print('Kha')
elif x >= 5:
    print('Trung binh')
else:
    print('Yeu')  

print('Ket thuc chuong trinh')      