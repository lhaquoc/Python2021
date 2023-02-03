#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 23:00:55 2022

@author: anhquoc
"""

def get_formatted_name(first_name, last_name):
    return (first_name + ' ' + last_name).title()

while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' at any time to quit!")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")