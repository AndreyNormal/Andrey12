# class House():
#     """описание дома"""
#     def __init__(self,street,number):
#         "свойства дома"
#         self.street = street
#         self.number = number

#         def build(self):
#             """строить дом"""
#             print("Дом на улице" + self.street + " под номером" + self.number + " Построим.")

#             house1 = House("Алматы", 20)
#             house2 = House("Алматы", 21)

#             print(house2.number)

# x = lambda a: a + 10
# print(x(5))

# x = lambda a,b,c: a  + b + c
# print(x(5,6,2))

# def say_hello(username,age):

#     print(f'Hello there{username}!')
#     print(f'age {age}!')


# say_hello("Andrey",20)
# say_hello("Andrey1",30)
# say_hello("Andrey2",40)

def myfunc(n):
    return lambda a: a*n
mydoubler = myfunc(2)