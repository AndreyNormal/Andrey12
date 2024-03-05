# 1)Write a Python program with builtin function to multiply all the numbers in a list


# returns the product of all the numbers in the list 'numbers'
# def list_multiply(numbers):

#   # We use product to 'build' the result of multiplying all the numbers in the 
#   # list, by multiplying each number by product and storing the result into 
#   # product.  We start product off at 1 so that when the first number in the 
#   # list is multiplied by product the number itself is the result.
#   product = 1

#   # have the for loop go through each number in the list
#   for number in numbers:
    
#     # output the values of product, number, and product*number so we can see 
#     # how the loop computes the return value
#     print(product,'x',number,'=',product*number)
    
#     # multiply the number in the list by product and store the result back into
#     # product 
#     product = product * number
  
#   # return the resulting product
#   return product 

# # test list should result in 60 as 2 x 3 x 5 x 2 = 60
# list1 = [2,3,5,2]

# # test out the list_multiply function
# print(list_multiply(list1))




#2) Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

# def string_test(s):
#     cases = {"Upper_case": 0,"Lower_case": 0}
 
#   # Create a dictionary 'd' to store the count of upper and lower case characters
#         # Iterate through each character
#     for character in str:
#         if character.isupper():
#               # If 'character' is upper case, increment the count of upper case characters in the dictionary
#             cases["Upper_case"] +=1
#         elif character.islower():
#             cases["Lower_case"] +=1
#         else:
#              # If 'c' is neither upper nor lower case (e.g., punctuation, spaces), do nothing
#             pass
#         print("Original string: ",str)
#         print("No for string", cases["Upper_case"])
#         print("No for character")

#         string_test("The quick ")
#3) Write a Python program with builtin function that checks whether a passed string is palindrome or not.
    
# def findPslindrome(s):

#             return s == s[::-1]  
#         #code for test
# s ="mallam"
# a =findPslindrome(s)

# if a:
#             print("Yes")
# else:
#             print("No")

#4)Write a Python program that invoke square root function after specific milliseconds.

# number = input("Sample input in millsec: ")

# number_sqrt = (float(number) /10)**0.5
# print("Square root of ", number, " is ",number_sqrt)
#5)Write a Python program with builtin function that returns True if all elements of the tuple are true.
# num = [23, 45, 10, 30]
# print(all(num)) #True

# # all values false
# num = [0, False]
# print(all(num)) #False

# # one false value
# num = [1, 3, 4, 0]
# print(all(num)) #False

# # one true value
# num = [0, False, 5]
# print(all(num)) #False

# # empty iterable
# num = []
# print(all(num)) #True