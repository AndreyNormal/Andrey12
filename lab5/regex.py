# 1)Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
# import re
# str=input("enter string:")
# pattern=r"ab+?"
# x = bool(re.search(pattern,str))
# print(x)

# 2)Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

# import string
# str=input("enter string:")
# pattern=r"ab+?"
# x = bool(string.search(pattern,str))
# print(x)
# 3)Write a Python program to find sequences of lowercase letters joined with a underscore.

# import re
# str =input('enter string:ab')
# pattern=r'ab+?'
# x=bool(re.search(pattern,str))
# print(x)
# 4)Write a Python program to find the sequences of one upper case letter followed by lower case letters.
# import re

# name = input ("Enter a file:")
# hand = open (name,'r')
# for line in hand:
#     line = line.rstrip()
#     str = re.findall('ab{0,1}',line)
#     print (str)
# 5)Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# import re

# name = input ("Enter a file:")
# hand = open (name,'r')
# for line in hand:
#     line = line.rstrip()
#     str = re.findall('ab{3}',line)#str = re.findall('abbb',line)
#     print (str)


# 6)Write a Python program to replace all occurrences of space, comma, or dot with a colon.

# import re

# name = input ("Enter a file:")
# hand = open (name,'r')
# for line in hand:
#     line = line.rstrip()
#     str = re.findall('ab{2,3}',line)
#     print (str)

# 7)Write a python program to convert snake case string to camel case string.
# import re

# name = input ("Enter a file:")
# hand = open (name,'r')
# for line in hand:
#     line = line.rstrip()
#     str = re.findall('[A-Z]{1}}_\S+[a-z]',line)
#     print (str)

# 8)Write a Python program to split a string at uppercase letters.

# import re

# name = input ("Enter a file:")
# hand = open (name,'r')
# for line in hand:
#     line = line.rstrip()
#     str = re.findall('[A-Z]{1}}_\S+[a-z]',line)
#     print (str)

# 9)Write a Python program to insert spaces between words starting with capital letters.

# import re

# name = input ("Enter a file:")
# hand = open (name,'r')
# for line in hand:
#     line = line.rstrip()
#     str = re.findall('^a.*$b\w',line)
#     print (str)

# 10)Write a Python program to convert a given camel case string to snake case.
# import re

# name = input ("Enter a file:")
# hand = open (name,'r')
# for line in hand:
#     line = line.rstrip()
#     str = re.findall('^\w+',line)
#     print (str)