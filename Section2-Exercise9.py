'''
9. Write a Python class which has two methods get_String and print_String.
get_String accept a string from the user and print_String print the string in upper case.
  
'''

class Class1:
    def __init__(self):
        self.str1 = ""
    def get_String(self):
        self.str1 = input("Please enter a string : ")
    def print_String(self):
        print(self.str1)


c1 = Class1()
c2 = Class1()

c1.get_String()
c1.print_String()

c2.get_String()
c2.print_String()