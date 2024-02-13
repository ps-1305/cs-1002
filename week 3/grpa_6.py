"""
Problem statement:
make a pyramid 
1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1
this is for n=5
n>=2
"""

n = int(input())
for i in range(1, n+1):
    for j in range(1, i):
        print(j, end=',')
    print(i, end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(1, i):
        print(j, end=',')
    print(i, end="")
    print()

# code by 23f202268
