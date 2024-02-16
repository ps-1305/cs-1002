"""
Problem statement:
Merging two strings and sorting them 
"""

a , b = input(), input()
n1, n2 = len(a), len(b)
x = a+b
x = sorted(x)
for i in range(len(x)):
    print(x, end="")
