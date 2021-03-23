class Encap():
    __rate=7
    def __calculate_amount(self,input):
        return input*self.__rate

    def normalmethod(self):
        print("this is normal method")

    def getrate(self):
        return self.__rate

    def setrate(self,a):
        self.__rate = a

gg = Encap()
print(gg._Encap__rate)
gg.setrate(54)
print(gg._Encap__calculate_amount(45))

print(gg.getrate())

gg.normalmethod()