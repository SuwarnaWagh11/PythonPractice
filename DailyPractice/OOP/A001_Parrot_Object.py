# An OBJECT is an entity has attribute and behavior
# parrot -
    # attribute: Name, Age, Color
    # behavior: Dancing, Singing

# CLASS is the blueprint of that object

class Parrot:

    # attribute
    name: str = ""
    age: int = 0


# create Parrot object 
p1 = Parrot()  # p1 is the reference of that class Parrot() which has 2 attribute
p2 = Parrot()
print(p1)
p1.age = 32
p1.name = "Suwarna"
p2.age = 35
p2.name = "Randhir"

print(p1.age, "----", p1.name)
print(p2.age, "----", p2.name)
