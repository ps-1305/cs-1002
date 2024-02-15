"""
Problem statement:
To check whether a string is palindrome or not
"""
s = input()
i = 0
j = len(s)-1
while i!=j:
    if s[i] != s[j]:
        print("NOT PALINDROME")
        exit()
    i += 1
    j -= 1
print("PALINDROME")
