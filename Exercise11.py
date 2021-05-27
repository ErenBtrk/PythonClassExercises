'''
11. Write a Python class named Student with two attributes student_id,
student_name. Add a new attribute student_class. Create a function to
display the entire attribute and their values in Student class.

'''

from inspect import isfunction

def function2():
    pass

class Student:
    student_id = "123"
    student_name = "Ali"
    def function():
        for attr,value in Student.__dict__.items():
            if(not attr.startswith('_') and not isfunction(value)): # isfunction()"Return true if the object is a user-defined function."
                print(f"{attr}->{value}")


setattr(Student,"student_class","ABC")


Student.function()

