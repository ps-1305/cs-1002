"""
Problem statement:
Accept a positive integer n as input and print the first 
n integers on a line separated by a comma.
"""

n = int(input())
for i in range(1,n):
    print(i, end=',')
print(n)
