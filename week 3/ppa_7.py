"""
Problem statement:
Accepting a positive integer and printing the sum of digits
"""

n, s = int(input()), 0
for i in range(len(str(n))):
    s += n%10
    n //= 10
print(s)
