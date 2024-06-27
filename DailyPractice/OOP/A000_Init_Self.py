""" Python is OOP
    self represent the instance of class which allows have it's own attribute and method of each obj in python
    self makes it easier to distinguish between the instance attribute & methods from local variables.
    self - whenever we create any class and define any method in it we make self as a first argument/parameter.
    we have c1 & c2 are the object of class Cat which holds the value of name & color using self keyword

    __init__() - First parameter if this is always the object, this function is called immediately 
    after the object is created and it is used to initialize the variables
    __init__() is used to initialize a newly created object while
    __new__() is used to control the way an object is created.
    """


class Cat:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def info(self):
        print(f'This is my cat name {self.name} and color is {self.color}')

    def make_sound(self):
        print("meow")

    @staticmethod
    def stat_meth():
        print("Off Topic method")


c1 = Cat("Gopi", "White")
c2 = Cat("Manu", "Orange")
c1.info()
type(c1.info)
print(type(c1.info))  # o/p -> <class 'method'>
print(type(Cat.info))  # o/p -> <class 'function'>
# In python Object itself being passed as the first argument to the corresponding function
Cat.info(c1)  # o/p -> This is my cat name Gopi and color is White
Cat.info(c2)  # o/p -> This is my cat name Manu and color is Orange

# line 24 type(c1.info) is same as Class.info(c1)
# i.e. object c1 is passed as first argument to the info() function.
# that is why first parameter of the function must be the object itself.

# if you don't want to use self - you can avoid it by using function decorator - @staticmethod 
Cat.stat_meth()
c1.stat_meth()
c2.stat_meth
