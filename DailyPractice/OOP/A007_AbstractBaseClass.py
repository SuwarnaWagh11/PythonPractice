# We can use ABC module to create Abstract classes in python
# we can use @abstractmethod decorator to create abstract method
# CUrrent version of Python in my machine is 3.11.4

from abc import ABC, ABCMeta, abstractmethod


class PolygonTest(ABC):

    @abstractmethod
    def number_of_sides(self):
        pass


class Triangle(PolygonTest):

    def number_of_sides(self):
        print("This method is implementation of polygonTest abstractmethod for Triangle")


class Square(PolygonTest):

    def number_of_sides(self):
        print("This method is implementation of polygonTest abstractmethod for Square")


t1 = Triangle()
t1.number_of_sides()

s1 = Square()
s1.number_of_sides()