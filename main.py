# Завдання 3
# Створіть базовий клас «Домашня тварина» та похідні
# класи «Пес», «Кіт», «Папуга», «Хом’як». За допомогою
# конструктора встановіть ім’я кожної тварини та її характеристики.
# Реалізуйте для кожного із класів наступні методи:
# ■ Sound — видає звук тварини (пишемо текстом в консоль);
# ■ Show — відображає ім’я тварини;
# ■ Type — відображає підвид тварини.

class DomesticAnimal:
    def __init__(self, name, type_of_animal):
        self.name = name
        self.type_of_animal = type_of_animal

    def sound(self):
        pass
    def show(self):
        print(f"Ім'я: {self.name}")
    def type(self):
        pass
class Dog(DomesticAnimal):
    def sound(self):
        print("Woof!")

    def show(self):
        super().show()

    def type(self):
        print(f"Тип тварини: {self.type_of_animal}")

class Cat(DomesticAnimal):
    def sound(self):
        print("Meow!")

    def show(self):
        super().show()

    def type(self):
        print(f"Тип тварини: {self.type_of_animal}")

class Parrot(DomesticAnimal):
    def sound(self):
        print("Ку-ка-рі-ку")
    def show(self):
        super().show()
    def type(self):
        print(f"Тип тварини: {self.type_of_animal}")

class Hamster(DomesticAnimal):
    def sound(self):
        print("звуки гризуна")

    def show(self):
        super().show()

    def type(self):
        print(f"Тип тварини: {self.type_of_animal}")

dog = Dog("Rey", "dog")
dog.sound()
dog.show()
dog.type()
print()
cat = Cat("Murchuk", "cat")
cat.sound()
cat.show()
cat.type()
print()
parrot = Parrot("Kuzya", "parrot")
parrot.sound()
parrot.show()
parrot.type()
print()
hamster = Hamster("Busya", "hamster")
hamster.sound()
hamster.show()
hamster.type()
print()