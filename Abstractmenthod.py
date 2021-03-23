from abc import ABC, abstractmethod


# Abstract Class
class ABSclass(ABC):

    def __init__(self):
        self.Age = 23
        self.name = "Kunal"

    @abstractmethod
    def display(self):
        print("display method")

    @abstractmethod
    def show(self):
        print("Show method")

    def ShowInfo(self):
        print("Age is: " + str(self.Age))
        print("Name is: " + str(self.name))


class Derived1(ABSclass):

    def __init__(self, surname, weight):
        super().__init__()
        self.SN = surname
        self.wt = weight

    def display(self):
        print("Derived display method")

    def show(self):
        print("Derived Show method")

    def ShowAllinfo(self):
        print("Surname is: " + str(self.SN))
        print("Weight is: " + str(self.wt))



d1 = Derived1(54, "navin")
d1.display()
d1.ShowInfo()
