<<<<<<< HEAD
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



# temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")

# # Extract the numerical part of the temperature and convert it to an integer
# degree = int(temp[:-1])

# # Extract the convention part of the temperature input (either 'C' or 'F')
# i_convention = temp[-1]

# # Check if the input convention is in uppercase 'C' (Celsius)
# if i_convention.upper() == "C":
#     # Convert the Celsius temperature to Fahrenheit
#     result = int(round((9 * degree) / 5 + 32))
#     o_convention = "Fahrenheit"  # Set the output convention as Fahrenheit
# # Check if the input convention is in uppercase 'F' (Fahrenheit)
# elif i_convention.upper() == "F":
    
#     result = int(round((degree - 32) * 5 / 9))
#     o_convention = "Celsius"  
# else:
  
#     print("Input proper convention.")
#     quit()

# # Display the converted temperature in the specified output convention
# print("The temperature in", o_convention, "is", result, "degrees.") 

# из цельсии в фаренгейты и конвертируйте в список с темпиратурами map


# def myfunc(Celsuis):
# #   return len(Celsuis)
# return (5/9)*(F-32)

#  F = 93
#  Celsius = myfunc(F)

#  print("C is " + Celsius)

# x = map(myfunc, ('celsius', 'farengeit', 'temperature'))

# print(x)

# #convert the map into a list, for readability:
# print(list(x))









#10Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def signiflist(S)
    x=[]
    for i in s:
        if i not in x:
            x.append(i)
            return x
        print(signiflist[1,2,3,4,5,6,7,8])





#11Write a Python function that checks whether a word or phrase is palindrome or 
        #not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def isPal(string):
    leftpos = 0
    rightpos = len(string)-1
    while rightpos >=leftpos:
        if not string[leftpos] == string[rightpos]:
            return False
        leftpos +=1
        rightpos -=1


#12Define a functino histogram() that takes 
        #a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
def histogram(inputList):
 
    for i in range(len(inputList)):
        print (inputList[i]*'*')
 
 
List = [4,9,7]
 
histogram(List)





#13Write a program able to play the "Guess the number" 
#- game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
import random, sys


def guess_number(num):
    random_number = random.randint(1,20)
    if random_number == num:
        print (" guess was ok it was")
        return 1 
    else:
        print (" U mistake here it was" + str(random_number))
        	return 0
    

if __name__=="__main__":
    
    name = str(raw_input("what is your name ?:"))
    print 
    print ("Well"+name+ "I am thinking of a number between 1 and 20.")
    for i in range(0, 5):
        num = int(raw_input("Take a  guess \n "))
	result = guess_number(num)
	if result:
	    sys.exit(1)

#14

##Farengeit and celsius
# def celsius(fareng):
#       return (fareng - 32)*(5/9)
# x = map(fareng,("F"))
# def Farengeit(celsius):
#    return ((celsius*(9/5)) + 32)
# x = map(Farengeit,("C"))

# print(x(lamba("Celcius")))


class Vehicle:
    def class

    
=======
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



# temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")

# # Extract the numerical part of the temperature and convert it to an integer
# degree = int(temp[:-1])

# # Extract the convention part of the temperature input (either 'C' or 'F')
# i_convention = temp[-1]

# # Check if the input convention is in uppercase 'C' (Celsius)
# if i_convention.upper() == "C":
#     # Convert the Celsius temperature to Fahrenheit
#     result = int(round((9 * degree) / 5 + 32))
#     o_convention = "Fahrenheit"  # Set the output convention as Fahrenheit
# # Check if the input convention is in uppercase 'F' (Fahrenheit)
# elif i_convention.upper() == "F":
    
#     result = int(round((degree - 32) * 5 / 9))
#     o_convention = "Celsius"  
# else:
  
#     print("Input proper convention.")
#     quit()

# # Display the converted temperature in the specified output convention
# print("The temperature in", o_convention, "is", result, "degrees.") 

# из цельсии в фаренгейты и конвертируйте в список с темпиратурами map


# def myfunc(Celsuis):
# #   return len(Celsuis)
# return (5/9)*(F-32)

#  F = 93
#  Celsius = myfunc(F)

#  print("C is " + Celsius)

# x = map(myfunc, ('celsius', 'farengeit', 'temperature'))

# print(x)

# #convert the map into a list, for readability:
# print(list(x))









#10
def signiflist(S)
    x=[]
    for i in s:
        if i not in x:
            x.append(i)
            return x
        print(signiflist[1,2,3,4,5,6,7,8])





#11
def isPal(string):
    leftpos = 0
    rightpos = len(string)-1
    while rightpos >=leftpos:
        if not string[leftpos] == string[rightpos]:
            return False
        leftpos +=1
        rightpos -=1


#12
def histogram(inputList):
 
    for i in range(len(inputList)):
        print (inputList[i]*'*')
 
 
List = [4,9,7]
 
histogram(List)





#13
import random, sys


def guess_number(num):
    random_number = random.randint(1,20)
    if random_number == num:
        print (" guess was ok it was")
        return 1 
    else:
        print (" U mistake here it was" + str(random_number))
        	return 0
    

if __name__=="__main__":
    
    name = str(raw_input("what is your name ?:"))
    print 
    print ("Well"+name+ "I am thinking of a number between 1 and 20.")
    for i in range(0, 5):
        num = int(raw_input("Take a  guess \n "))
	result = guess_number(num)
	if result:
	    sys.exit(1)

#14

##
def celsius(fareng):
      return (fareng - 32)*(5/9)
x = map(fareng,("F"))
def Farengeit(celsius):
   return ((celsius*(9/5)) + 32)
x = map(Farengeit,("C"))

>>>>>>> dd8f882a758c64afd814387123f34671af6bcf0f
