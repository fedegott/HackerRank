"""Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of .

Sample Input 0

2
1 2
Sample Output 0

3713081631934410656"""



# input 2 and 1 2

### hash() --> Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup.
##  Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).

n = int(input()) # 2
integer_list = map(int, input().split()) # type is list
#  1 2  # convert the split string into int
t = tuple(integer_list)
print( hash( t ))### function is hash(xxx), it gives the unique hash value that identifies the tuple