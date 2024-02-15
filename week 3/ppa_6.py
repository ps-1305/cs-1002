"""
Problem statement:
To take input of strings and print the shortest
"""

arr = []
while True:
    x = input()
    if x != 'abcdefghijklmnopqrstuvwxyz':
        arr.append(x)
        continue
    break
min = arr[0]
for i in range(len(arr)):
    if len(arr[i]) < len(min):
        min = arr[i]
print(min)
