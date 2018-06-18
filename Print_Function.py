# if __name__ == '__main__':
""" Read an integer N

Without using any string methods, try to print the following:

123.....N
"""

n = int(input())
i = 1
a = ''

while i <= n:
    a += '{}'.format(i)
    i += 1
print(a)