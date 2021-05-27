'''
10. Write a Python class named Student with two attributes student_id, student_name.
Add a new attribute student_class and display the entire attribute and their values
of the said class. Now remove the student_name attribute and display the entire 
attribute with values.

'''

class Student:
    student_id = "123"
    student_name = "Ali"


setattr(Student,"student_class","V") # Adding new attribute

print("\nAfter adding a new attribute :\n ")
for attr,value in Student.__dict__.items():
    if(not attr.startswith('_')):
        print(f"{attr} -> {value}")

delattr(Student,"student_name")

print("\nAfter deleting an attribute :\n ")
for attr,value in Student.__dict__.items():
    if(not attr.startswith('_')):
        print(f"{attr} -> {value}")