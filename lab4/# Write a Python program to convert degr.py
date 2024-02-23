# 1)Write a Python program to convert degree to radian.
# import math
# def degrees_to_radians(degrees):
#     return degrees * (math.pi / 180)
# degrees = float(input("Enter angle in degrees: "))
# radians = degrees_to_radians(degrees)
# print(f"{degrees} degrees is equal to {radians} radians")

#2)Write a Python program to calculate the area of a trapezoid.
# base_1 = 5
# base_2 = 6
# height = float(input("Height of trapezoid: "))
# base_1 = float(input('Base one value: '))
# base_2 = float(input('Base two value: '))
# area = ((base_1 + base_2) / 2) * height
# print("Area is:", area)

#3)Write a Python program to calculate the area of regular polygon.

# from math import tan, pi
# n_sides = int(input("Input number of sides: "))
# s_length = float(input("Input the length of a side: "))
# p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
# print("The area of the polygon is: ",p_area)

#4)Write a Python program to calculate the area of a parallelogram.
# base = float(input('Length of base: '))
# height = float(input('Measurement of height: '))
# area = base * height
# print("Area is: ", area)