"""
You are given the dates of birth of two persons, not necessarily from the same family. Your task is to find the younger of the two. 
If both of them share the same date of birth, 
then the younger of the two is assumed to be that person whose name comes first in alphabetical order (names will follow Python's capitalize case format).

The input will have four lines. The first two lines correspond to the first person, 
while the last two lines correspond to the second person. For each person, 
the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format. Your output should be the name of the younger of the two.
"""
name1 = input()
date1 = list(map(str, input().split("-")))
name2 = input()
date2 = list(map(str, input().split("-")))

if int(date1[2]) < int(date2[2]):
    print(name2)
elif int(date1[2]) > int(date2[2]):
    print(name1)
else:
    if int(date1[1]) < int(date2[1]):
        print(name2)
    elif int(date1[1]) > int(date2[1]):
        print(name1)
    else:
        if int(date1[0]) < int(date2[0]):
            print(name2)
        elif int(date1[0]) > int(date2[0]):
            print(name1)
        else:
            if ord(name1[0]) > ord(name2[0]):
                print(name2)
            else:
                print(name1)
