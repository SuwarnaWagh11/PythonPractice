# An object is an entiry has attribute and behavior 
# parrot -
    # attribute: Name, Age, Color
    # behavior: Dancing, Singing

# class is the bluprint of that object

class Parrot:

    # attribute
    name: str = ""
    age: int = 0

# create Parrot object 
p1 = Parrot() # p1 is the reference of that class Parrot() which has 2 attribute
print(p1)
p1.age = 32
p1.name = "Suwarna"

print(p1.age, "----", p1.name)