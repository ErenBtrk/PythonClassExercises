'''
9. Write a Python class named Student with two attributes student_name, marks.
Modify the attribute values of the said class and print the original and modified
values of the said attributes.
  
'''


class Student:
    student_name = "Ali"
    marks = 123

s1 = Student()

print(getattr(Student,'student_name'))
print(getattr(Student,"marks"))

setattr(Student,"student_name","Veli")
setattr(Student,"marks",123456)

print(getattr(Student,'student_name'))
print(getattr(Student,"marks"))
