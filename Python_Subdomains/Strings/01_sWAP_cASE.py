"""You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format
A single line containing a string .
Constraints

Output Format
Print the modified string .
Sample Input 0
HackerRank.com presents "Pythonist 2".
Sample Output 0
hACKERrANK.COM PRESENTS "pYTHONIST 2"."""


 # use if want to input
s = 'AAaBbccDDEe'
sample = 'HackerRank.com presents "Pythonist 2".'
def swap_case(string_):
    word = ''
    for i in string_:
        if i.islower():
            i = i.upper()
            word += i
        else:
            i = i.lower()
            word += i
    # print(word)
    return word

print(swap_case(s))
print(swap_case(sample))
# print(__name__)


if __name__ == '__main__':
    print("please input a string:")
    string = input()
    result = swap_case(string)
    print(swap_case(result))
# else:


### using a list comprehension ####

# print (''.join([i.lower() if i.isupper() else i.upper() for i in input()])) # note that it uses ''.join to add each character to the string and input() inside the list comprehension
