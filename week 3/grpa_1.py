"""
Problem statement:
Accept a positive integer n as input and print the sum of the first n terms of the series given below:
1 + (1+2) + (1+2+3) + ...
"""

n = int(input())
temp = 0
s = 0
for i in range(1, n+1):
    temp += i
    s += temp
print(s)
