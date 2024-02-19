string = list(map(str, input().split(" ")))
word = input()
if word in string:
    print("YES")
    print(string.count(word))
    exit()
print("NO")
