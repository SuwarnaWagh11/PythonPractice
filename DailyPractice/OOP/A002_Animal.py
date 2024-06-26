# base class
class Animal:
    def eat(self):
        print("I am eating")
    
    def sleep(self):
        print("I am sleeping")

class Dog(Animal):
    def bark(self):
        print("I am barking")

a1 = Animal()
a1.eat()
a1.sleep()

d1 = Dog()
d1.eat()
d1.sleep()
d1.bark()