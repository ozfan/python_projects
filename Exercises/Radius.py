#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:54:18 2020

@author: ivan
"""

# Ask the user for the radius of a circle and then print the area
# radius = int(input("What is the radius of the square? \n >>> "))
# area = radius * 3.14159 **2
# print("You entered {} as the radius. The area of this square is {}"
#       .format(radius, area))

#Convert fahrenheit to celsius

# far = float(input("Please enter the temperature in Fahrenheit: \n >>> "))
# cel = (far - 32) * 5/9
# print("You entered {} degrees Fahrenheit, which is {} degrees Celsius"
#       .format(far, cel))

# Obtain the sum of two integers

# num_1 = int(input("Please enter the first number: \n >>> "))
# num_2= int(input("Please enter the second number: \n >>> "))
# print("The sum of " + str(num_1) + " and " + str(num_2) + " is " 
#       + str(num_1 + num_2))

# Obtain the product of two integers

# num_1 = int(input("Please enter the first number: \n >>> "))
# num_2= int(input("Please enter the second number: \n >>> "))
# product = num_1 * num_2
# print("The product of", num_1, "and", num_2, "is", product)

# Bob, Ann, Jane and Ashwin want to order pizza - they know they will each eat
# 4 slices of pizza. The local pizza shop sells pizzas of only 6 slices
# What is the minimum number of pizzas needed - Use floor division

total_slices = 4 * 4
number_of_pizzas = (total_slices + 5) // 6
slices_left = (number_of_pizzas * 6) - total_slices
print("There will need to be a total of at least", total_slices, 
      "slices of pizza and you'll need to order at least", number_of_pizzas,
      "pizzas and will have", slices_left, "slices leftover")