
class Sorting:

    def swap(self,a,b):
        temp = 0
        temp = a
        a = b
        b = temp
        return a,b

    def swap_addition(self,a,b):
        a = a+b
        b = a-b
        a = a-b
        return a, b

    def swap_multi(self,a,b):
        a = a*b
        b = a/b
        a = a/b

    def Sorting_alogo(self,inputlist):

        temp = 0
        for i in range(len(inputlist)):
            for k in range(i+1,len(inputlist)):
                if inputlist[i] > inputlist[k]:
                    inputlist[i],inputlist[k] = self.swap(inputlist[i],inputlist[k])

        print(inputlist)

inputlist1 = [1,6,7,12,3,9,97,8,5,3,2,4,7,88,93645,153,486]
obj = Sorting()
obj.Sorting_alogo(inputlist1)

