"""
Problem statement:
Accept a string as input, convert it to lower case, sort the string in alphabetical order, and print the sorted string to the console. You can assume that the string will only contain letters.
"""
x = input()
y = x.lower()
z = sorted(y)
for i in range(len(z)):
    print(z[i], end="")

# code by 23f202268
