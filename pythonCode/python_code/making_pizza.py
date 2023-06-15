#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 00:04:09 2022

@author: anhquoc
"""
# Importing an Entire Module
import pizza
pizza.make_pizza(22, 'shrimp', 'pineapple')
pizza.make_pizza(16, 'green peppers', 'mushroom')

# Importing Specific Functions
from pizza import make_pizza
make_pizza(22, 'shrimp', 'pineapple')
make_pizza(16, 'green peppers', 'mushroom')

# Using as to Give a Function an Alias
from pizza import make_pizza as mp
mp.make_pizza(22, 'shrimp', 'pineapple')
mp.make_pizza(16, 'green peppers', 'mushroom')

# Using as to Give a Module an Alias
import pizza as p
p.make_pizza(16, 'peperoni')
p.make_pizza(22, 'mushrooms', 'green peppers')

# Importing All Functions in a Module
from pizza import *
make_pizza(15, 'toppings')