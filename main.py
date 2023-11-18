# Завдання 4
# Створіть базовий клас Employer (службовець) з функцією Print(). Функція має виводити інформацію про службовця.
# Для базового класу це може бути рядок із написом
# «This is Employer class».
# Створіть від нього три похідні класи: President, Manager, Worker. Перевизначте функцію Print() для виведення
# інформації, що відповідає кожному типу службовця.
# Завдання 5
# Для класів із попереднього завдання реалізуйте магічний метод str, а також метод int (який повертає вік
# службовця).

class Employer:
    def __init__(self, age):
        self.age = age

    def print_info(self):
        print("This is Employer class")

    def __str__(self):
        return f"Employer (Age: {self.age})"

    def get_age(self):
        return self.age

class President(Employer):
    def print_info(self):
        print("This is President class")

    def __str__(self):
        return f"President (Age: {self.age})"

class Manager(Employer):
    def print_info(self):
        print("This is Manager class")

    def __str__(self):
        return f"Manager (Age: {self.age})"

class Worker(Employer):
    def print_info(self):
        print("This is Worker class")

    def __str__(self):
        return f"Worker (Age: {self.age})"

# Приклад використання:
employer = Employer(30)
employer.print_info()
print(str(employer))
print("Age:", employer.get_age())

president = President(age=45)
president.print_info()
print(str(president))
print("Age:", president.get_age())

manager = Manager(age=35)
manager.print_info()
print(str(manager))
print("Age:", manager.get_age())

worker = Worker(age=25)
worker.print_info()
print(str(worker))
print("Age:", worker.get_age())


