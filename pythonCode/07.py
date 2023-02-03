#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:33:42 2022

@author: anhquoc
"""

x = 1
print(type(x))

x = 1.0
print(type(x))

x = 1 + 3j;
print(type(x))

x = "ABC"
print(type(x))

x = True
print(type(x))

x = None
print(type(x))

e = 2.65
pi = "3.14"
s = "Hello Python"

print("Kieu du lieu cua e: {0}, Kieu du lieu cua pi: {1}, Kieu du lieu cua s: {2}".format(type(e), type(pi), type(s)))
print("Kieu du lieu cua e: ", type(e), ", Kieu du lieu cua pi: ", type(pi), ", Kieu du lieu cua s: ", type(s))