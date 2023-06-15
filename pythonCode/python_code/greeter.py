#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 23:31:21 2022

@author: anhquoc
"""

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title())

greet_user('quoc')

# Default Values
def describe_pet(pet_name, animal_type='dog'):
    print("I have a " + animal_type + ".")
    print("Its name is " + pet_name + ".")
    
describe_pet("Tom")
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')