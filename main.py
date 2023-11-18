# Завдання 1
# Створіть базовий клас «Фігура» з методом для підрахунку площі. Створіть похідні класи: прямокутник, коло,
# прямокутний трикутник, трапеція, зі своїми методами для підрахунку площі.

import math
class Figure:
    def __init__(self, name):
        self.name = name

class Rectangle(Figure):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Triangle(Figure):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Trapezium(Figure):
    def __init__(self, name, a, b, height):
        super().__init__(name)
        self.a = a
        self.b = b
        self.height = height

    def area(self):
        return 0.5 * (self.a + self.b) * self.height

# Приклад використання:
rectangle = Rectangle("Прямокутник", 4, 6)
print(f"{rectangle.name}: Площа = {rectangle.area()}")

circle = Circle("Коло", 5)
print(f"{circle.name}: Площа = {circle.area()}")

triangle = Triangle("Прямокутний трикутник", 3, 4)
print(f"{triangle.name}: Площа = {triangle.area()}")

trapezium = Trapezium("Трапеція", 2, 5, 3)
print(f"{trapezium.name}: Площа = {trapezium.area()}")
