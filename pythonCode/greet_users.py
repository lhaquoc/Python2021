#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 23:06:50 2022

@author: anhquoc
"""

def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
