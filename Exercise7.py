'''
7. Write a simple Python class named Student and display its type.
Also, display the __dict__ attribute keys and the value of the
__module__ attribute of the Student class. 

'''

class Student:
    def __init__(name,age):
        student_name = name
        student_age = age
        

print(type(Student))

print(Student.__dict__.keys())

print(Student.__module__)