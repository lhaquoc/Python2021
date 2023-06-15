#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:20:08 2022

@author: anhquoc
"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Restaurant's name is " + self.restaurant_name.title() + ".")
        print("The cuisine type is " + self.cuisine_type.title() + ".")
        
    def open_restaurant(self):
        print(self.restaurant_name + " is opening")
        
        
my_restaurant = Restaurant('Snuff Corner', 'Texan')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('Phuc Loc Tho', 'Vietnamese')
your_restaurant.describe_restaurant()