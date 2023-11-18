# Завдання 1
# Використовуючи поняття множинного успадкування,
# створіть клас «Коло, поміщене в квадрат».

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

class CircleInSquare(Circle, Square):
    def __init__(self, radius, side):
        self.circle = Circle(radius)
        self.square = Square(side)

    def remaining_area(self):
        return self.square.area() - self.circle.area()

circle_in_square = CircleInSquare(5, 10)

print("Площа круга:", circle_in_square.circle.area())
print("Площа квадрата:", circle_in_square.square.area())
print("Залишкова площа:", circle_in_square.remaining_area())

#Варіант 2

