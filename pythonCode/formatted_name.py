#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:56:54 2022

@author: anhquoc
"""
def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
