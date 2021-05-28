'''
10. Write a Python class named Rectangle constructed by a length and width
and a method which will compute the area of a rectangle.

'''

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def method(self):
        return self.length * self.width


rec1 = Rectangle(10.0,5.0)
print(rec1.method())

rec2 = Rectangle(8.5,4.0)
print(rec2.method())