"""
Problem statement:
Accept a positive integer n, with n > 1 as input from the user and print all the prime factors of n in ascending order.
"""

def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False;
    return True;

n = int((input()))
flag = 0
for i in range(2, n):
    if n % i == 0 and prime(i):
        print(i)
        flag = 1
if flag == 0:
    print(n)
