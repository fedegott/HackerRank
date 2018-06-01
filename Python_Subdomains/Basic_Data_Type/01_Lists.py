"""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]"""

"input:"
'''
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print'''


# to see out paste the above commands
N = 12

alist = []
for _ in range(N): ###It's just a variable name, and it's conventional in python to use _ for throwaway variables. It just indicates that the loop variable isn't actually used
    string_ =str(input()).split() # ## why raw_input() instead of input()? -->in raw_input() you give input as string while in input() as a interger.  .split() do split by whitespace
    # print(string_)
    command = string_[0]
    # print(string_[0])
    arguments = string_[1:]
    # print(string_[1:])
    if command != 'print':
        command += "("+",".join(arguments)+")" #join() is string method which takes either a string or List of strings as parameters ex:- join("hai") or join(["hai","bye"])
# the "," before .join() is DELIMITER. means by using comma JOIN joins the hai and bye so ",".join(["hai","bye"]) gives you hai,bye
#         print(','.join('3' '4')) # --> output is 3,4
        # print(command)
        eval("alist."+command) ### The eval function lets a python program run python code within itself. I'ts considered bad practice to use it
    # print(alist)
    else:
        print (alist)


