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
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def show(self):
        print(f"Тип фігури: {self.shape_type}")

    def save(self, file):
        file.write(f"Тип фігури: {self.shape_type}\n")


class Square(Shape):
    def __init__(self, top_left_x, top_left_y, side_length):
        super().__init__("Квадрат")
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.side_length = side_length

    def show(self):
        super().show()
        print(f"Координати верхнього лівого кута: ({self.top_left_x}, {self.top_left_y})")
        print(f"Довжина сторони: {self.side_length}")

    def save(self, file):
        super().save(file)
        file.write(f"Верхній лівий кут: {self.top_left_x}, {self.top_left_y}\n")
        file.write(f"Довжина сторони: {self.side_length}\n")

    @classmethod
    def load(cls, file):
        top_left_x, top_left_y = map(int, file.readline().split(":")[-1].strip().split(", "))
        side_length = int(file.readline().split(":")[-1].strip())
        return cls(top_left_x, top_left_y, side_length)


class Rectangle(Shape):
    def __init__(self, top_left_x, top_left_y, length, width):
        super().__init__("Прямокутник")
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.length = length
        self.width = width

    def show(self):
        super().show()
        print(f"Координати верхнього лівого кута: ({self.top_left_x}, {self.top_left_y})")
        print(f"Довжина: {self.length}")
        print(f"Ширина: {self.width}")

    def save(self, file):
        super().save(file)
        file.write(f"Верхній лівий кут: {self.top_left_x}, {self.top_left_y}\n")
        file.write(f"Довжина: {self.length}\n")
        file.write(f"Ширина: {self.width}\n")

    @classmethod
    def load(cls, file):
        top_left_x, top_left_y = map(int, file.readline().split(":")[-1].strip().split(", "))
        length = int(file.readline().split(":")[-1].strip())
        width = int(file.readline().split(":")[-1].strip())
        return cls(top_left_x, top_left_y, length, width)


class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__("Коло")
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def show(self):
        super().show()
        print(f"Координати центру: ({self.center_x}, {self.center_y})")
        print(f"Радіус: {self.radius}")

    def save(self, file):
        super().save(file)
        file.write(f"Кординати центру: {self.center_x}, {self.center_y}\n")
        file.write(f"Радіус: {self.radius}\n")

    @classmethod
    def load(cls, file):
        center_x, center_y = map(int, file.readline().split(":")[-1].strip().split(","))
        radius = int(file.readline().split(":")[-1].strip())
        return cls(center_x, center_y, radius)


class Ellipse(Shape):
    def __init__(self, left_top_x, left_top_y, width, height):
        super().__init__("Еліпс")
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.width = width
        self.height = height

    def show(self):
        super().show()
        print(f"Координати верхнього лівого кута: ({self.left_top_x}, {self.left_top_y})")
        print(f"Розміри прямокутника: ({self.width}, {self.height})")

    def save(self, file):
        super().save(file)
        file.write(f"Кординати верхнього кута: ({self.left_top_x}, {self.left_top_y})\n")
        file.write(f"Розміри прямокутника: ({self.width}, {self.height})\n")

    @classmethod
    def load(cls, file):
        left_top_str = file.readline().split(":")[-1].strip()
        left_top_x, left_top_y = map(int, left_top_str[1:-1].split(","))
        width_str = file.readline().split(":")[-1].strip()
        height_str = file.readline().split(":")[-1].strip()
        width, height = map(int, width_str[1:-1].split(","))
        return cls(left_top_x, left_top_y, width, height)



# Створення фігур та збереження їх у файл
shapes = [
    Square(0, 0, 5),
    Rectangle(1, 1, 6, 4),
    Circle(0, 0, 3),
    Ellipse(2, 2, 5, 3)
]

filename = "shapes.txt"
with open(filename, 'w') as file:
    for shape in shapes:
        shape.show()
        shape.save(file)
        file.write("\n")

# Завантаження фігур з файлу та відображення інформації про них
loaded_shapes = []
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        shape_type = line.split(":")[-1].strip()
        if shape_type == "Квадрат":
            loaded_shape = Square.load(file)
        elif shape_type == "Прямокутник":
            loaded_shape = Rectangle.load(file)
        elif shape_type == "Коло":
            loaded_shape = Circle.load(file)
        elif shape_type == "Еліпс":
            loaded_shape = Ellipse.load(file)

        loaded_shapes.append(loaded_shape)

        line = file.readline()

# Ві





