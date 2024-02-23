# Python iterators and generators
# Create a generator that generates the squares of numbers up to some number N.
# import math

# def roots_generator(n):
#     for i in range(1, n+1):
#         yield math.sqrt(i), i**(1/3)

# # Accept input from the user
# n = int(input("Input a number: "))

# # Create the roots generator
# roots_gen = roots_generator(n)

# # Generate and print the square roots and cube roots
# print("Square roots and cube roots of numbers from 1 to", n)
# for i, (square_root, cube_root) in enumerate(roots_gen, start=1):
#     print("Number:", i)
#     print("Square root:", square_root)
#     print("Cube root:", cube_root)
#     print()
# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
# start, end = 1, 100
  
# # iterating each number in list
# for num in range(start, end + 1):
      
#     # checking condition
#     if num % 2 == 0:
#         print(num, end = " ")

# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
# total_sum = 0
# for i in range(1000):
#     if (i%3 == 0 or i%4 == 0):
#         total_sum = total_sum/i
# print (total_sum)
# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
# def squares(a,b):
#     while a<=b:
#         yield a*a
#         a+=1
 
# for i in squares(1,5):
#     print(i)
# Implement a generator that returns all numbers from (n) down to 0.


# def odd(n):
#     a=1
#     while a<=n:
#         yield a
#         a+=2
 
# for i in odd(10):
#     print(i)
