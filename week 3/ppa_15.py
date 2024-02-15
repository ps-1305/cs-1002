"""
Problem statement:
Accept a string as input, print Integer if the string is an integer, print Float if it a float, else print None.
"""

x = input()
for i in x:
    if i not in '1234567890.':
        print(None)
        exit()
if "." in x:
    print("Float")
    exit()
print("Integer")
