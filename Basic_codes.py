# a = [1, 56, 96, 1, 9, 3, 78, 31, 45]
#
# # a.sort()
# # print(a)
#
# # Ascending
#
# temp = 0
# for i in range(len(a)):
#     for j in range(i+1 , len(a)):
#         if a[i]>a[j]:
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
#
#
# print(a)
#

# def sqrtfun(i):
#     ans = i ** (2)
#     print(ans)
#
# sqrtfun(9)

# Linear Search
# a=[1,5,7,9,3,1,47,89,5,3,4,9,3,1,1]
# searching = 6516
# cnt=0
# for i in range(len(a)):
#     if a[i]==searching:
#         cnt=cnt+1
#         print("number found at position "+str(i))
#
# if cnt==0:
#     print("Not Found")
# print("Total count "+str(cnt))

# def binarysearch(list,searching):
#
#     lower = 0
#     upper = len(list)
#
#     while upper >= lower:
#         mid = (lower+upper) // 2
#
#         if list[mid] == searching:
#             print("Element found at position: "+str(mid))
#             return True
#         else:
#             if list[mid] < searching:
#                 lower = mid
#             else:
#                 upper = mid
#
# a=[1,5,7,9,3,1,47,89,5,3,4,9,3,1,1]
# binarysearch(a,1)
#
# print(7//2)


s='Kuaenlsta'

Vow=['a','e','i','o','u','A','E','I','O','U']

# for i in range (len(s)):
#     print(s[i])
#
#     if s[i].isupper():
#         print("upper")
#         output = output + s[i].lower()
#     else:
#         print("Lower")
#         output = output + s[i].upper()
#
#
# print(output)
cnt=0
maxcnt=0
for i in range(len(s)):

    if s[i] in Vow:
        cnt=cnt+1
        if cnt > maxcnt:
            maxcnt=cnt
    else:
        cnt = 0

print("Largest answer: "+str(maxcnt))