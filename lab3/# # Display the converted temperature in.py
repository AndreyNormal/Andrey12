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


def myfunc(Celsuis_to_Farengeit):
    return (5/9)*(F-32)

F = 93
Celsius = myfunc(F)

Celsius_to_Farengeit = map(myfunc,('celsius', 'farengeit'))

print(Celsius_to_Farengeit)