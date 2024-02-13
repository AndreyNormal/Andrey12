# Python Function
# A recipe you are reading states how many grams you need for the ingredient. Unfortunately, 
#your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams

# def myfunc(x):
# 	return 28.3495231 * x
# ## return нужен, чтобы функция что-то возвращала
# grams = 5
# ounces = myfunc(grams)

# print (ounces)


# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature.
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)
# def myfunc(F):
#     return (5/9)*(F-32)

# F = 93
# Celsius = myfunc(F)

# print("C is " + Celsius)

	

# Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
# def solve(numheads, numlegs):
# numheads =35
# numlegs = 94
# NoSolution = "No solution"
# for i in range (numheads + 1 ):
#     s = numheads - i
#     if  2 * i + 4 * s == numlegs:
#         return i,j
#     return NoSolution,NoSolution

# solution = solve(numheads, numlegs)
# print (solution)
# You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers 
#as an agrument and returns only prime numbers from the list.
# import math
# def  filter_prime(num1,num2):
#  primeNumber = []
#  for num in range (num1,num2 + 1):
#   if Prime(num):
#    primeNumber.append(num)
#    return primeNumber
  
#   def Prime(number):
#    if number <= 1:
#     return False
#    sqrtNumber = int(math.sqrt(number))
#    for num in range(2, sqrtNumber + 1):
#     if number % num ==0:
#      return False
#     return True
   
#    print(filter_prime(0,20))
   
# Write a function that accepts string from user and print all permutations of that string.
# from itertools import permutations

# lst = ["".join(p) for p in permutations("day")]
# print(lst)
# Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

# txt = "New York"

# rev = txt[::-1]

# print("Reversed =", rev)

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# def has_33(nums):
#     pass

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
# Write a function that takes in a list of integers and returns True if it contains 007 in order
# def spy_game(nums):
#     pass

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
# Write a function that computes the volume of a sphere given its radius.

# Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

# Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

# Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

# ****
# *********
# *******
# Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
# Hello! What is your name?
# KBTU

# Well, KBTU, I am thinking of a number between 1 and 20.
# Take a guess.
# 12

# Your guess is too low.
# Take a guess.
# 16

# Your guess is too low.
# Take a guess.
# 19

# Good job, KBTU! You guessed my number in 3 guesses!
# Create a python file and import some of the functions from the above 13 tasks and try to use them.

