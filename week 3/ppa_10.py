"""
Problem statement:
sum of all prime numbers from [1,n]
"""

def prime(n):
    k = n
    if n%2 != 0: k += 1
    for i in range(2,int(k/2+1)):
        if n%i == 0:
            return False
    return True
num, s = int(input()), 2
for i in range(3, num+1):
    if prime(i):
        s += i
print(s)
