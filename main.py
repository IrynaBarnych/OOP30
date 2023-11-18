#конспект
#множинне успадкування
class A:
    def say_hello(self):
        print("Hello from class A")
class B(A):
    def say_hello(self):
        print("Hello from class B")
class C(A):
    def say_hello(self):
        print("Hello from class C")
class D(C, B):
    def say_hello(self):
        super().say_hello()
        A().say_hello()
obj1 = A()
obj1.say_hello()
obj = D()
obj.say_hello()
print(D.mro())
print(D.__mro__)

#ex1
class C:
    def __init__(self):
        print('c')


class A:
    def __init__(self):
        print('a')


class B(A):
    def __init__(self):
        super().__init__()
        print('b')


class D(B, A):
    def __init__(self):
        super().__init__()
        # A.__init__(self)
        print('d')


obj = D()