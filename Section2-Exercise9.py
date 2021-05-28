'''
9. Write a Python class named Student with two attributes student_name, marks.
Modify the attribute values of the said class and print the original and modified
values of the said attributes.
  
'''

class Student:
    student_name = "Ali"
    marks = "123"

for attr,value in Student.__dict__.items():
    if(not attr.startswith('_')):
        print(f"{attr}->{value}")

setattr(Student,"student_name","Veli")
setattr(Student,"marks","456")

for attr,value in Student.__dict__.items():
    if(not attr.startswith('_')):
        print(f"{attr}->{value}")

