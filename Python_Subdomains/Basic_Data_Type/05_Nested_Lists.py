"""Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints


There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry"""

# from operator import itemgetter
# a = {'c':0,'a':1, 'b':2}
# ### can not sorted the values or keys in dict, but can use sorted
# #which generates a sorted list
# d = sorted(a) # generates sorted list by keys
# e = sorted(a.items(), key= itemgetter(1)) ### generates new  sorted list by values. need to import from operator import itemgetter__
# print(type(d) ,'\n', type(e))

# for _ in range(int(input())):
#         name = input()
#         score = float(input())
#
# from operator import itemgetter
#
# name = ['Harry', 'Berry', 'Tina', 'Akriti','Harsh']
# score = [37.21, 37.21, 37.2, 41, 39]
#
#
# name_score = list(zip(name,score)) ### this is a nested list (or list of lists)
#
# sort_name_score = sorted(name_score,key= lambda name_score:name_score[1]) #### sort using the 2nd column
# sort_name_score1 = sorted(name_score,key= itemgetter(1)) ### another way to sort by second column. need to import from operator import itemgetter
# # print(sort_name_score)
# #if not xxx arugment:
# #       raise ValueError('no argument in function'
#
# min_ = min(sort_name_score, key = lambda sort_name_score: sort_name_score[1]) # used key similarly to sorted
#
#
# while min(name_score, key=itemgetter(1)) == min_:
#
#     name_score.remove(min(name_score, key= itemgetter(1))) ### removes a value, not the index
#
# min_1 = min(name_score, key = itemgetter(1))
#
# index_ =[]
# for i in range(len(name_score)):
#
#
#     if name_score[i][1] == min_1[1]:
#
#         index_.append(name_score[i][0])
#     sort_ = sorted(index_)
# for j in sort_:
#     print (j)


###### ALternativy solution ########

# N = int(input())
# students = []
# for i in range(N):
#     grade = [input(), float(input())]
#     students.append(grade)
# students = sorted(students, key=lambda x: x[1])
# second_highest = students[0][1]
# for name, grade in students: # loops over the 2 variables
#     if grade > second_highest:
#         second_highest = grade
#         break
# print('\n'.join([name for name, grade in sorted(students) if grade == second_highest]))

#### without input ####

# N = int(input())
students = []
# for i in range(N):
    # grade = [input(), float(input())]

name = ['Harry', 'Berry', 'Tina', 'Akriti','Harsh']
score = [37.21, 37.21, 37.2, 41, 39]
grade= [name, score]
students.append(grade)

students = sorted(students, key=lambda x: x[1])
second_highest = students[0][1]
for name1, grade1 in students:
    print(grade1)
    if grade1 > second_highest:
        second_highest = grade1
        break
print(grade1)
# print('\n'.join([name1 for name1, grade1 in sorted(students) if grade1 == second_highest]))