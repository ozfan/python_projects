# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:17:56 2019

@author: giles
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''
# class Account(object):
#     ''' Bank Account Attributes'''
#     '''------------------------------'''
#     ''' Check Balance '''
#     ''' Withdraw Balance '''
#     ''' Deposit Balance '''
    
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
    
#     def check_balance(self):
#         print(f'Hello {self.name}, your current balance: {self.balance}')
        
#     def withdraw(self):
#         amount_out = float(input("How much would you like to withdraw? >> "))
#         if amount_out > self.balance:
#             print(f'You do not have enough funds to withdraw, your balance is \
#                   {self.balance}.')
#         else:
#             self.balance -= amount_out
#             print(f'You withdrew {amount_out} and your current balance is {self.balance}.')
        
#     def deposit(self):
#         amount_in = float(input("How much would you like to deposit? >> "))
#         self.balance += amount_in
#         print(f'You deposited {amount_in} and your current balance is {self.balance}.')
    


'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''
import math

class Circle(object):
    ''' Calculation of the area of the circle '''
    
    def __init(self, radius):
        self.radius = radius
    
    def cal_radius(self):
        area = math.pi * (self.radius) ** 2
        print(f'The radius you entered is {self.radius} and the area is {area}.')

