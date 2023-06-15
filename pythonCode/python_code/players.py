#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 17:00:41 2022

@author: anhquoc
"""
players = ['tom', 'paul', 'son', 'hung', 'thang', 'james', 'jane', 'mary']

# Slicing a List
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[:-3])
print(players[-3:])

# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())