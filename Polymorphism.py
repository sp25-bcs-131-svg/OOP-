#Opereator Overloading

class Complex():

    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self, other):
        newReal = self.real + other.real
        newImg = self.img + other.img
        return Complex(newReal,newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

#Method Overriding (Inheritance)

class Animal():

    def speak(self):
        print("I can speak")

class Dog(Animal):

    def speak(self):
        print("Woof!")

class Cat(Animal):

    def speak(self):
        print("Meow!")

animals : list[Animal] = [Dog(),Cat(),Animal()]

for animal in animals:
    animal.speak()

#Method Overeloading

class Calculator():

    def add (self,a,b,c=0):
        return a+b+c

calc = Calculator()
print(calc.add(5,10))
print(calc.add(5,10,15))