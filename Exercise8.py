'''
8. Write a Python program to crate two empty classes, Student and Marks.
Now create some instances and check whether they are instances of the said classes or not.
Also, check whether the said classes are subclasses of the built-in object class or not.

'''

class Student:
    pass
class Marks:
    pass

s1 = Student()
s2 = Student()

m1 = Marks()
m2 = Marks()

print(isinstance(s1,Student))
print(isinstance(s2,Student))
print(isinstance(m1,Marks))
print(isinstance(m2,Marks))

print(issubclass(Student, object))
print(issubclass(Marks, object)) 