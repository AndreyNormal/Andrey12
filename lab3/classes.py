<<<<<<< HEAD
#1)Define a class which has at least two methods:
# getString: to get a string from console input printString: to print the string in upper case.
class StringfromInput(object):
    def __init__(itself):
        itself.s = ""

    def getString(itself):
        itself.s = input()
    
    def printString(itself):
        print(itself.s.upper())

Objectfromstring = StringfromInput()
Objectfromstring.getString()
Objectfromstring.printString()



#2)Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class NameShape:
    
    name = "NameShape"
    
    def __init__(self, name = None):
    
        self.name = name

jeffrey = NameShape("Jeffrey")
print ("NAme this person")
nico = NameShape()
nico.name = "Nico"
print ("Name this person") % (NameShape.name, nico.name)

#3)Define a class named Rectangle which inherits from Shape class from task 
#2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.


#4)Write the definition of a Point class. Objects from this class should have a
    #a method dist that computes the distance between 2 points

    import math

p = [3]
q = [1]

print (math.dist(p, q))

p = [3, 3]
q = [6, 12]

print (math.dist(p, q))


#5)Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals,
# and test to make sure the account can't be overdrawn.
class Accout():
    def myfunc(itself):
        itself = 0
       
    def depositOfBank(itself,sum):
        itself_balance += sum
        return itself_balance
    
    def withdraw(itself,sum):
             if itself_balance < sum: raise
             itself_balance -=sum
             return itself_balance
    print("No money")

#6)Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
    def primalnum(list):
         for i in range(1,5):
          print(i)
          return filter(lambda x:x == i or x % i,list)
         
         def primalnum2(list):
             num = list
             for i in range(2,8):
                 print i 
                 num = filter(lambda x:x == i or x % i,num)
                 return num
             print (primalnum([2,3,4,5,6,7,8,9,10,11]))
            

=======
#1)Define a class which has at least two methods:
# getString: to get a string from console input printString: to print the string in upper case.
class StringfromInput(object):
    def __init__(itself):
        itself.s = ""

    def getString(itself):
        itself.s = input()
    
    def printString(itself):
        print(itself.s.upper())

Objectfromstring = StringfromInput()
Objectfromstring.getString()
Objectfromstring.printString()



#2)Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class NameShape:
    
    name = "NameShape"
    
    def __init__(self, name = None):
    
        self.name = name

jeffrey = NameShape("Jeffrey")
print ("NAme this person")
nico = NameShape()
nico.name = "Nico"
print ("Name this person") % (NameShape.name, nico.name)

#3)Define a class named Rectangle which inherits from Shape class from task 
#2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class reCircle:
    def __init__(itself, color, filled, radius):
        itself.__color = color
        itself.__filled = filled
        itself.__radius = radius      

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled

    def get_area(self):
        return math.pi * self.__radius ** 2



#4)Write the definition of a Point class. Objects from this class should have a
    #a method dist that computes the distance between 2 points

    import math

p = [3]
q = [1]

print (math.dist(p, q))

p = [3, 3]
q = [6, 12]

print (math.dist(p, q))


#5)Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals,
# and test to make sure the account can't be overdrawn.
class Accout():
    def myfunc(itself):
        itself = 0
       
    def depositOfBank(itself,sum):
        itself_balance += sum
        return itself_balance
    
    def withdraw(itself,sum):
             if itself_balance < sum: raise
             itself_balance -=sum
             return itself_balance
    print("No money")

#6)Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
    def primalnum(list):
         for i in range(1,5):
          print(i)
          return filter(lambda x:x == i or x % i,list)
         
         def primalnum2(list):
             num = list
             for i in range(2,8):
                 print i 
                 num = filter(lambda x:x == i or x % i,num)
                 return num
             print (primalnum([2,3,4,5,6,7,8,9,10,11]))
            

>>>>>>> dd8f882a758c64afd814387123f34671af6bcf0f
