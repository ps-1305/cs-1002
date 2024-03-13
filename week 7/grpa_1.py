all = []
for _ in range(8):
    temp = list(map(str, input().split(",")))
    all.append(temp)
    temp = []
for i in range(8):
    print(f"{all[i][0]}:{len(all[i])-1}")
