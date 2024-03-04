"""
Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers.
"""
no = list(map(str, input().split(',')))
prod = 1
for i in range(len(no)):
    prod *= int(no[i])
print(prod)
