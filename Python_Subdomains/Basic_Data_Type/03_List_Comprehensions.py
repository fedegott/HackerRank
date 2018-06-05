"""Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here,

Input Format

Four integers  and  each on four separate lines, respectively.

Constraints

Print the list in lexicographic increasing order.

Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
Explanation 0

Concept

You have already used lists in previous hacks. List comprehensions are an elegant way to build a list without having to use different for loops to append values one by one. This example might help.

Example: You are given two integers x and y . You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y) This is the code if we dont use list comprehensions in Python.

python x = int ( raw_input()) y = int ( raw_input()) n = int ( raw_input()) ar = [] p = 0 for i in range ( x + 1 ) : for j in range( y + 1): if i+j != n: ar.append([]) ar[p] = [ i , j ] p+=1 print ar
Other smaller codes may also exist, but using list comprehensions is always a good option. Code using list comprehensions:

python x = int ( raw_input()) y = int ( raw_input()) n = int ( raw_input()) print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]

Sample Input 1

2
2
2
2
Sample Output 1

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
Easy
Submitted 59219 times
Max Score 10
Need Help?

View Tutorial
View Discussions
View Editorial Solution
View Top Submissions
RATE THIS CHALLENGE

Download problem statement
Download sample test cases
Suggest Edits
Current Buffer (saved locally, editable)
"""
# def list_compr (X, Y, Z, N):
#     list_c = [[i, j, k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if ( (i+j+k) != N) ]
#     ### notice output is i,j,k between [] and notice if conditional
#     return print(list_c)
#
# list_compr(1,1,1,2)

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())
list_c = [[i, j, k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if ( (i+j+k) != N) ]
print(list_c)