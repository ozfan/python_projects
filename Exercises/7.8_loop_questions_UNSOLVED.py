#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Giles
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
# num_1 = int(input("Please enter a number between 1-100: >> "))
# num_2 = int(input("Please enter another number between 1-100: >> "))

# while num_1 < 0 or num_2 < 0 or num_1 > 100 or num_2 > 100 or num_1 == num_2:
#     print("Numbers must be different values between 1 and 100, please try again!")
#     num_1 = int(input("Please enter a number between 1-100: >> "))
#     num_2 = int(input("Please enter another number between 1-100: >> "))

# if num_1 < num_2:
#     for i in range(num_1, num_2+1):
#         print(i, end = " ")
        
# else:
#     for i in range(num_2, num_1+1):
#         print(i, end = " ")

'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''

# word = input("Please input a word: >> ")

# print(word[::-1])


'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
# num = int(input("Please input a number between 1 and 12: >>> "))

# while num < 1 or num > 12:
#     print("The number is not between 1 and 12, please try again!")
#     num = int(input("Please input a number between 1 and 12: >>> "))
    
# for x in range(1, 13):
#     print(str(num) + " x " + str(x) + " = " + str(num * x))


'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''


# for x in range(1, 13):
#     for i in range(1, 13):
#         print(str(i) + " x " + str(x) + " = " + str(i * x))



'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
# user_input = input("Please enter a number or type exit to stop: >> ")
# numbers = []

# while user_input.lower() != "exit":
#     while not user_input.isdigit():
#         print("That is not a number, please input a number: >> ")
#         user_input = input("Try again: >> ")
#     numbers.append(int(user_input))
#     user_input = input("Please enter the next number: >> ")

# mean = sum(numbers) / len(numbers)

# print("The mean of the numbers you put in is " + str(mean))



'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''

n = 15
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i

print(factorial)


'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''



'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''



'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
