"""
Problem statement: 
take n positive integer inputs into an array and print the maximum value
"""

arr = []
while True:
    x = int(input())
    if x != 0:
        arr.append(x)
        continue
    break
max = arr[0]
for i in range(len(arr)):
    if max<arr[i]:
        max = arr[i]
print(max)

# code by 23f202268
