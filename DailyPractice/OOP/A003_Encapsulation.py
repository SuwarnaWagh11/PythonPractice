# ENCAPSULATION
# Data Hiding - Where w bundle the Class attributes & methods in a way to prevent outer classes from accessing it.
# How? we can define private attribute with _ or __ as prefix and __init__() method to store them

class Computer:

    def __init__(self) -> None:
        self.__max_sell_price = 900

    def sell(self):
        print("Max selling price is {}".format(self.__max_sell_price))

    def setMaxPrice(self, price):
        self.__max_sell_price = price


c1 = Computer()
c1.sell()
c1.__max_sell_price = 1000
c1.sell()
c1.setMaxPrice(1200)
c1.sell()
#  here we accessed the __max_Sell_price and set 1000 initially but it is private attribute of the Computer class
#  in order to set value in private attribute, we need to access setter method of Computer class.
