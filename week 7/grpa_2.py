all = dict()
lens = []
for _ in range(8):
    temp = list(map(str, input().split(",")))
    all[temp[0]] = len(temp)-1
    lens.append(len(temp)-1)
    temp = []
lens = sorted(lens)
another = dict()
for j in lens:
    for i in all.keys():
        if all[i] == j:
            another[i] = j
for i in range(len(another)-1,-1,-1):
    print(f"{list(another.keys())[i]}:{list(another.values())[i]}")
