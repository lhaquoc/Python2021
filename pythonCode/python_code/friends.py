#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 23:05:34 2022

@author: anhquoc
"""

names = ['Tom', 'Paul', 'Chris', 'Peter', 'Jane', 'Luna']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

message = "Hello, {0}, good to see you!"
print(message.format(names[0]))
print(message.format(names[1]))
print(message.format(names[2]))
print(message.format(names[3]))
print(message.format(names[4]))
print(message.format(names[5]))