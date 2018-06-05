"""
Find the Runner-Up (Second Place) Score!

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints



Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5

"""

######Using Numpy ######

# import numpy as np
#
# def runner_up (n, array):
#
#     max = arr.max()
#     temp = 0
#     j= 1
#     while (max-j) != 0:
#         for i in arr:
#             if i == max-j:
#                 print(i)
#                 return ### the function will stop the first time it print(i), otherwise it will print i for max-1, max-2, etc
#         # print(j)
#         j += 1
#
#
# arr = np.array([2,3,6,6,5]) # note that need to put array between []
# runner_up(5, arr)

##### Without Numpy #######
# def runner_up1():
#     # n = int(input())
#     # arr = map(int, input().split())
#     arr = [2,3,6,6,5]
#     arr1 = list(arr)
#
#     #Find Max
#     max = 0
#     for i in arr1:
#         if max < i:
#             max = i
#     j = 1
#     while (max - j) != 0:
#         for i in arr1:
#                 if i == max-j:
#                     print(i)
#                     return
#         j += 1
#
#
# runner_up1()

#####Solve without Function#####

# arr = [2,3,6,6,5]
#
#
# #Find Max
# max = 0
# for i in arr:
#     if max < i:
#         max = i
#
# for j in range(len(arr)+1):
#     j += 1
#     # print(j)
#     for i in arr:
#         if i == max-j:
#             print(i)
#             temp  = i
#     if temp == max-j:
#         break

### HackerRank Solution ####
# i = int(input())
# lis = list(map(int,input().strip().split()))[:i]
# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))
#
# print (max(lis))

### alternatively I could sort the list first###

# i = int(input())
# lis = list(map(int,input().strip().split()))[:i]
lis = [2,3,6,6,6,4]
alist = sorted(lis)
# print(alist)
for i in range(len(alist)):
    i += 1
    n = len(alist) - i

    # print (alist[len(alist)-1])
    if alist[n] == alist[len(alist)-1]:
        # print(alist[n-1])
        a = 1
    else:
        print (alist[n])
        break

# while max(lis) == z:
#     lis.remove(max(lis))
#
# print (max(lis))