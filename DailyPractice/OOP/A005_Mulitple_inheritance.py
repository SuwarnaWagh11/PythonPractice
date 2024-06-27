class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")


class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")


class Bat(Mammal, WingedAnimal):
    def bat_method(self):
        print("Super Class method called")

class Mouse(Mammal):
    def mouse_method1(self):
        print("Super Class method called")


class Mice(Mouse):
    def mice_method(self):
        print("Super Class method called")


# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()
