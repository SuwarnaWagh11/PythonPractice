# INHERITANCE
# base class
class Animal:
    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")


# derived class
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

a2 = Dog()
a2.bark()
# derived class Dog can access members of the base class Animal. It's because Dog is inherited from Animal.
