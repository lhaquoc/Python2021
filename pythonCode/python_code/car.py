#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 11:03:45 2022

@author: anhquoc
"""


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('audi', 'a6', 2022)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(38)
my_new_car.read_odometer()
my_new_car.update_odometer(28)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2010)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(2000)
my_used_car.read_odometer()
my_used_car.increment_odometer(50)
my_used_car.read_odometer()
