"""In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.


Sample Input

ABCDCDC
CDC

Sample Output
2

"""


def count_substring(string, sub_string):
    count = int()
    for i in range(len(string)):

        # get length of substring and do rolling window across the string, counting the number of times it matches
        rolling_window = string[i:(len(sub_string)+i)]
        # print(rolling_window)
        if rolling_window == sub_string:
            count += 1



    return count

string1= 'ABCDCDC'
sub_string1= 'CDC'

print(count_substring(string1, sub_string1))