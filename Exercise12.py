'''
12. Write a Python class named Student with two instances student1,
student2 and assign given values to the said instances attributes.
Print all the attributes of student1, student2 instances with their
values in the given format.

'''

class Student:
    student_name = "Ali"
    student_id = 123

student1 = Student()
student2 = Student()

student1.student_name = "Veli"
student1.student_id = 234

student2.student_name = "Ayse"
student2.student_id = 555
student2.marks_language = 85
student2.marks_science = 70
student2.marks_math = 65

students = [student1,student2]

for s in students:
    for attr in s.__dict__:
        print(f"{attr} -> {getattr(s,attr)}")
