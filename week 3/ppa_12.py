"""
Problem statement:
Accept two strings as input and form a new string by removing all characters from the second string which are present in the first string. 
Print this new string as output. 
You can assume that all input strings will be in lower case.
"""

x, y, z = input(), input(), ""
for i in y:
    if i not in x:
        z+=i
print(z)
