# Завдання 3
# Створіть базовий клас Shape для рисування плоских фігур.
# Визначте методи:
# ■ Show() — виведення на екран інформації про фігуру;
# ■ Save() — збереження фігури у файл;
# ■ Load() — зчитування фігури з файлу.
# Визначте похідні класи:
# ■ Square — квадрат із заданими з координатами лівого
# верхнього кута та довжиною сторони.
# ■ Rectangle — прямокутник із заданими координатами
# верхнього лівого кута та розмірами.
# ■ Circle — коло із заданими координатами центру та радіусом.
# ■ Ellipse — еліпс із заданими координатами верхнього кута
# описаного навколо нього прямокутника зі сторонами,
# паралельними осям координат, та розмірами цього прямокутника.
# Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну
# фігуру.



class Shape:
    def __init__(self, name):
        self.name = name  # Назва фігури

    def show(self):
        print(f"Shape: {self.name}")

    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(f"{self.name}")

    def load(self, filename):
        with open(filename, 'r') as file:
            self.name = file.readline().strip()


class Square(Shape):
    def __init__(self, left_top_x, left_top_y, side_length):
        super().__init__("Square")
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.side_length = side_length

    def show(self):
        super().show()
        print(f"Left Top: ({self.left_top_x}, {self.left_top_y}), Side Length: {self.side_length}")

    def save(self, filename):
        super().save(filename)
        with open(filename, 'a') as file:
            file.write(f"{self.left_top_x} {self.left_top_y} {self.side_length}\n")

    def load(self, filename):
        super().load(filename)
        with open(filename, 'r') as file:
            data = file.readline().split()
            self.left_top_x, self.left_top_y, self.side_length = map(int, data[1:])


class Rectangle(Shape):
    def __init__(self, left_top_x, left_top_y, width, height):
        super().__init__("Rectangle")
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.width = width
        self.height = height

    def show(self):
        super().show()
        print(f"Left Top: ({self.left_top_x}, {self.left_top_y}), Width: {self.width}, Height: {self.height}")

    def save(self, filename):
        super().save(filename)
        with open(filename, 'a') as file:
            file.write(f"{self.left_top_x} {self.left_top_y} {self.width} {self.height}\n")

    def load(self, filename):
        super().load(filename)
        with open(filename, 'r') as file:
            data = file.readline().split()
            self.left_top_x, self.left_top_y, self.width, self.height = map(int, data)


class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__("Circle")
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def show(self):
        super().show()
        print(f"Center: ({self.center_x}, {self.center_y}), Radius: {self.radius}")

    def save(self, filename):
        super().save(filename)
        with open(filename, 'a') as file:
            file.write(f"{self.center_x} {self.center_y} {self.radius}\n")

    def load(self, filename):
        super().load(filename)
        with open(filename, 'r') as file:
            data = file.readline().split()
            self.center_x, self.center_y, self.radius = map(int, data)


class Ellipse(Shape):
    def __init__(self, left_top_x, left_top_y, width, height):
        super().__init__("Ellipse")
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.width = width
        self.height = height

    def show(self):
        super().show()
        print(f"Left Top: ({self.left_top_x}, {self.left_top_y}), Width: {self.width}, Height: {self.height}")

    def save(self, filename):
        super().save(filename)
        with open(filename, 'a') as file:
            file.write(f"{self.left_top_x} {self.left_top_y} {self.width} {self.height}\n")

    def load(self, filename):
        super().load(filename)
        with open(filename, 'r') as file:
            data = file.readline().split()
            self.left_top_x, self.left_top_y, self.width, self.height = map(int, data)


# Створення фігур
square = Square(0, 0, 5)
rectangle = Rectangle(0, 0, 4, 6)
circle = Circle(0, 0, 3)
ellipse = Ellipse(0, 0, 4, 2)

# Створення списку фігур
figures = [square, rectangle, circle, ellipse]

# Збереження фігур у файл
for index, figure in enumerate(figures):
    figure.save(f"figure_{index}.txt")


loaded_figures = []

# Завантаження фігур з файлів
for index in range(len(figures)):
    loaded_figure = Square(0, 0, 0)
    loaded_figure.load(f"figure_{index}.txt")
    loaded_figures.append(loaded_figure)

# Відображення інформації про кожну фігуру
for figure in loaded_figures:
    print(figure)