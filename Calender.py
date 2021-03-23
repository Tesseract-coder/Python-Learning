import string
import datetime
import time

Sample1=[['9:00', '10:30'],['12:00','13:00'],['16:00','18:00']]
bound1=['9:00','20:00']

Sample2=[['10:00', '11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']]
bound2=['10:00','18:00']

# datetime_object = datetime.datetime.strptime('9:00', '%H:%M')
# datetime_object2 = datetime.datetime.strptime('10:00', '%H:%M')
# print(datetime_object2)
# print(datetime_object2-datetime_object)

def getstartime(inputlist):
    strttime=[]
    for i in range(len(inputlist)):
        temp=[]
        temp=inputlist[i]
        strttime.append(temp[0])
    return strttime

def getendtime(inputlist):
    strttime=[]
    for i in range(len(inputlist)):
        temp=[]
        temp=inputlist[i]
        strttime.append(temp[1])
    return strttime

# print(getstartime(Sample1))
# print(getstartime(Sample2))

# print(getendtime(Sample1))
# print(getendtime(Sample2))

def convert_to_time(inputlist):
    output1=[]
    for i in range(len(inputlist)):
        temp = datetime.datetime.strptime(inputlist[i],'%H:%M')
        output1.append(temp)
    return output1


def getfreetime(startlist,endlist,startbound,endbound):
    output=[]
    if startbound!=startlist[0]:
        output=[[startbound,startlist[0]]]

    for i in range(len(endlist)):
        templist = []
        temp1 = endlist[i]

        try:
            temp2 = startlist[i+1]
            if temp2==temp1:
                templist=[]
            else:
                templist = [temp1, temp2]
                output.append(templist)

        except: IndexError

    if endbound!=endlist[len(endlist)-1]:
        output.append([endlist[len(endlist)-1],endbound])

    return output

print(getfreetime(getstartime(Sample1),getendtime(Sample1),bound1[0],bound1[1]))
print(getfreetime(getstartime(Sample2),getendtime(Sample2),bound2[0],bound2[1]))

# Freetime_1=getfreetime(getstartime(Sample1),getendtime(Sample1),bound1[0],bound1[1])
# Freetime_2=getfreetime(getstartime(Sample2),getendtime(Sample2),bound2[0],bound2[1])

