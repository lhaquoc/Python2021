#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 23:13:39 2022

@author: anhquoc
"""

favorite_languages = {
    'jen': ['python', 'ruby'],
    'tom': ['java', 'go'],
    'sarah': ['c'],
    'phil': ['python', 'haskell'],
    'Paul': ['dart']
    }

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print("\n" + name.title() + "'s favorite language is:")
    else:
        print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())