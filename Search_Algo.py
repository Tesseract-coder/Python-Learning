from Sorting_Algo import Sorting


class Search(Sorting):

    def linear_search(self, list, num):
        cnt = 0
        loc = ''
        for i in range(len(list)):
            if list[i] == num:
                cnt = cnt + 1
                loc = loc + ' ' + str(i)

        if cnt == 0:
            print("Expected Number " +str(num)+ " is not present in list")

        else:
            print("Expected number: "+str(num)+ " is present at following location: "+loc)


    def binary_search(self, list,num):
        sortedlist = self.Sorting_alogo(list)
        low = 0
        upper = len(list) - 1

        while low <= upper:
            mid = (low+upper)//2

            if list[mid] == num:
                globals()['position'] = mid

            else:
                if list[mid] < num:
                    low = mid
                else:
                    upper = mid

            print("Expected Number is at: "+str(position))


obj = Search()
inputlist = [1, 5, 12, 89, 2, 3, 45, 4, 5, 6, 3, 789, 7, 8, 9]
obj.linear_search(inputlist,3)
obj.binary_search(inputlist,3)
