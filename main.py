# Завдання 1
# Створіть базовий клас «Фігура» з методом для підрахунку площі. Створіть похідні класи: прямокутник, коло,
# прямокутний трикутник, трапеція, зі своїми методами для підрахунку площі.
# Завдання 2
# Для класів із першого завдання перевизначте магічні методи int (повертає площу) та str (повертає інформацію
# про фігуру).

import math

class Figure:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def __int__(self):
        return int(self.area())  # Змінено на int(self.area())

    def __str__(self):
        return f"{self.name} - Площа, кв.м: {self.area()}"

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
print(str(rectangle))

circle = Circle("Коло", 5)
print(str(circle))

triangle = Triangle("Прямокутний трикутник", 3, 4)
print(str(triangle))

trapezium = Trapezium("Трапеція", 2, 5, 3)
print(str(trapezium))


