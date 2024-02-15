"""
Problem statement:
Two integers are co-prime if the only common divisor between the two integers is one.
Accept two positive integers as input in two different lines. 
Print Coprime if the two integers are co-prime, else print Not Coprime.
Assume that both the integers are greater than two.
"""

x , y = int(input()), int(input())
fx, fy = [], []
for i in range(2, x+1):
    if x%i == 0:
        fx.append(i)
for i in range(2, y+1):
    if y%i == 0:
        fy.append(i)
for i in range(len(fx)):
    if fx[i] in fy:
        print("Not Coprime")
        exit()
print("Coprime")
