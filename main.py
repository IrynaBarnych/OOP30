# Завдання 2
# Використовуючи механізм множинного успадкування, створіть клас «Автомобіль». Також мають бути класи:
# «Колеса», «Двигун», «Двері» та ін.

class Wheels:
    def __init__(self, count):
        self.count = count

class Engine:
    def __init__(self, power):
        self.power = power

class Doors:
    def __init__(self, open = False):
        self.open = open

class Car(Wheels, Engine, Doors):
    def __init__(self, count, power, open):
        Wheels.__init__(self, count)
        Engine.__init__(self, power)
        Doors.__init__(self, open)

car = Car(4,150, True)
print(car.__dict__)