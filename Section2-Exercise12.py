'''
12. Write a Python program to get the class name of an instance in Python.
'''

class Student:
    pass

class Teacher:
    pass

s1 = Student()
t1 = Teacher()

print(type(s1).__name__)
print(type(t1).__name__)