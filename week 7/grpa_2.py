def merge(d1: dict, d2: dict, priority: str)->dict:
    if priority == "first":
        temp = []
        for i in d1:
            for j in d2:
                if i == j:
                    temp.append(j)
        for word in temp:
            d2.pop(word)
    else:
        temp = []
        for i in d1:
            for j in d2:
                if i == j:
                    temp.append(i)
        for word in temp:
            d1.pop(word)
    d1.update(d2)
    return d1

