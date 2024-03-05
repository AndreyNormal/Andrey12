# 1)Write a Python program to list only directories, files and all directories, files in a specified path.
# import os
# all_files = os.listdir()
# print(all_files)
# 2)Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

# import os
# print(os.path.exists(r"C:\Users\user\Documents\work\lab4"))
# 3)Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
# import os
# print("Test a path exists or not:")
# path = r'g:\\testpath\\a.txt'
# print(os.path.exists(path))
# path = r'g:\\testpath\\p.txt'
# print(os.path.exists(path))
# 4)Write a Python program to count the number of lines in a text file.
# def file_lengthy(fname):
#         with open(fname) as f:
#                 for i, l in enumerate(f):
#                         pass
#         return i + 1
# print("Number of lines in the file: ",file_lengthy("test.txt"))
# 5)Write a Python program to write a list to a file.
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# with open('abc.txt', "w") as myfile:
#         for c in color:
#                 myfile.write("%s\n" % c)

# content = open('abc.txt')
# print(content.read())

# 6)Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

# import string, os
# if not os.path.exists("letters"):
#    os.makedirs("letters")
# for letter in string.ascii_uppercase:
#    with open(letter + ".txt", "w") as f:
#        f.writelines(letter)
#  7)Write a Python program to copy the contents of a file to another file
# from shutil import copyfile
# copyfile('test.py', 'abc.py')
# 8)Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
# import os
 
# # File name
# file = 'file1.txt'
 
# # File location
# location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
 
# # Path
# path = os.path.join(location, file)
 
# # Remove the file
# # 'file.txt'
os.remove(path)