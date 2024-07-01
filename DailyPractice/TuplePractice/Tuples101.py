# Tuples primarily used to store  data that does not change.
# i.e. it allows you to create immutable sequence of classes.
# tuples can store heterogeneous data like db records.
t1 = (1, 2, 3, 5, 1, 6, 2, 0, 1)
print(t1)
print(type(t1))
print(t1.count(1))
print(t1.index(2, 0, 3))
s = [(1, 'a'), (2, 'b')]
print(s, " is type of ", type(s))
"""Tuples and lists serve different purposes. Lists store homogenous data. You can and should have a list like this:

["Bob", "Joe", "John", "Sam"]
The reason that is a correct use of lists is because those are all homogenous types of data, specifically, people's names. But take a list like this:

["Billy", "Bob", "Joe", 42]
That list is one person's full name, and their age. That isn't one type of data. The correct way to store that information is either in a tuple, or in an object. Lets say we have a few :

[("Billy", "Bob", "Joe", 42), ("Robert", "", "Smith", 31)]
The immutability and mutability of Tuples and Lists is not the main difference. A list is a list of the same kind of items: files, names, objects. Tuples are a grouping of different types of objects. They have different uses"""