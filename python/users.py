#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:37:48 2022

@author: anhquoc
"""

user_0 = {
              'username': 'efermi',
              'first': 'enrico',
              'last': 'fermi',
              }

# Looping Through All Key-Value Pairs
for k, v in user_0.items():
    print("\nKey: " + k)
    print("\nValue: " + v)
    
# Looping Through All the Keys in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys():
    print("\nName: " + name.title())
    
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    if name in friends:
        print("Hi, " + name.title() + ", I see your favorite language is " + 
              favorite_languages[name].title() + "!")
        
# Looping Through a Dictionary’s Keys in Order
favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking poll.")
    
# Looping Through All Values in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())