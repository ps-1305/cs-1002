"""
Accept the date in DD-MM-YYYY format as input and print the year as output.
"""
date = list(map(str, input().split("-")))
print(date[2])
