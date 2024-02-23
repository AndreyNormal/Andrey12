# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# print(tuple1)
# print(tuple2)
# print(tuple3)

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)


# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# myset = {"apple", "banana", "cherry"}
# print(type(myset))

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")

# a = 33
# b = 33
# if b > a:
#     print("b is greater than a")
# elif a ==b:
#     print("a and b are equal")

# c = 200
# b =33
# if b > c:
#     print("b is greater that a")
# elif c == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")


# a = 200
# b =33
# if a > b: print ("a is greater than b")

# a = 2
# b = 330
# print("A") if a > b else print("B")

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#     print("Bath conditions are True")
# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")

# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")

# x = 11
# if x > 10:
#     print("Above ten,")
#     if x > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20.")

# if statements cannot be empty, but if you for some reason have a
# n if statement 
# with no content, put in the pass statement to avoid getting an error.
# a = 33
# b = 200
# if b > a:
#     pass

# i =1
# while i < 6:
#     print(i)
#     i +=1

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i +=1

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# x = bytearray(5)
# print(x)
# print(type(x))

# x = {"name" : "John", "age" : 36}

# #display x:
# print(x)

# #display the data type of x:
# print(type(x)) 

# dict это лист который нельзя изменить

# x = "awesome"

# def myfunc():
#     print("Python is" + x)

#     myfunc()

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)
