class Person:
    def __init__(self, Nature, Age, name):
        self.Nature = Nature
        self.Age = Age
        self.name = name

    def show_person_details(self):
        print("My name is " + self.name)
        print("My Age is " + str(self.Age))
        print("My Nature is " + self.Nature)


P1 = Person("Good", 24, "Kunal")
P1.show_person_details()


class Female(Person):
    def __init__(self,Nature,Age,name,Boobsize, figure, saree):
        super().__init__(Nature,Age,name)
        self.Boobsize = Boobsize
        self.Fig = figure
        self.saree = saree

    def new_method(self):
        self.show_person_details()
        print("Also Printing new method")





    # def show_Femail_details(self):


F1=Female("Goooooood",51651,"nana",32,"36-26-36","paithani")

F1.new_method()
