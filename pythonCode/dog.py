#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 09:53:47 2022

@author: anhquoc
"""

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        print(self.name.title() + " rolled over!")

# create an instance
my_dog = Dog('pooh', 5)
# accessing attributes
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# calling methods
my_dog.sit()
my_dog.roll_over()