'''
11. Write a Python class named Circle constructed by a radius and
two methods which will compute the area and the perimeter of a circle.

'''

class Circle:
    pi = 3.14
    def __init__(self,radius) -> None:
        self.radius = radius
    def area(self):
        return self.pi * (self.radius**2)
    def perimeter(self):
        return 2 * self.pi * self.radius

c1 = Circle(8.0)
print(f"c1 object's area = {c1.area()}\nc1 object's perimeter = {c1.perimeter()}")