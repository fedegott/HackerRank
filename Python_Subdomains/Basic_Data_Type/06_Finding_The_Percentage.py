"""You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for  students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

Constraints



Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0

56.00
Explanation 0

Marks for Malika are  whose average is

Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Sample Output 1

26.50"""

########### USING INPUT ##################
# import statistics
#
# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split() ### *line, all other splits get packaged into line
#     scores = list(map(float, line))
#     student_marks[name] = scores # creates anew row called name and adds scores as value
# query_name = input()
# aggre = student_marks[query_name]
# # for i in range(len(ave)):
# ave = statistics.mean(aggre)
# print(ave)
#
# if __name__ == '__main__':
#     print('a')
#
############ WITHOUT INPUT ################
"""should be:
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60"""

# import statistics
#
# s1 = 'Krishna \n Arjun \n Malika'
# s2 = [67, 70, 52]
# s3 = [68, 98, 56]
# s4 = [69, 63, 60]
#
# l1 = []
#
# for j in range(3):
#     l1.append([]) # needed to create nested list aka list of lists
#     for i in range(len(s2)):
#         i += 2
#         l1[j].append(eval('s{}[{}]'.format(i,j))) # s[2][0], then s[3][0], s[4][0], s[0][1], etc
# # output is nest list  [[67,68,69],[70,98,63],[52,56,60]]
# s = s1.split()
# dictio = dict(enumerate(l1)) #need to use dict(), {} does not work for enumerate
# print(dictio)
# ### to delete old key 0,1,2 and get new one s = 'Krishna \n Arjun \n Malika' can do:
# for i in range(3):
#     dictio[s[i]] = dictio[i]
#     dictio.pop(i) # need to eliminate original keys
# print(dictio)
#
# ave = statistics.mean(dictio['Malika'])
# print(ave)

######### SOLUTION ##########
marks = {}
for _ in range(int(input())):
    line = input().split()
    marks[line[0]] = list(map(float, line[1:]))
print('%.2f' % (sum(marks[input()]) / 3))
