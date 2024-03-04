"""
You are given a string and two non-negative integers as input. The two integers specify the start and end indices of a substring in the given string. 
Create a new string by replicating the substring a minimum number of times so that the resulting string is longer than the input string.
The input parameters are the string, start index of the substring and the end index of substring (endpoints inclusive) each on a different line.
"""
a = input()
st = int(input())
en = int(input()) + 1
b,c = a[st:en], a[st:en]
while len(a) >= len(b):
    b += c
print(b)
