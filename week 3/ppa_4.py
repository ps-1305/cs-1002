n = int(input())
if n%2 !=0: n+=1 
for i in range(2, int(n/2)):
    if n%i == 0:
        print("PRIME")
        exit()
print("NOTPRIME")
