def value_to_keys(D,value):
    l = []
    for i in D.keys():
        if D[i] == value:
            l.append(i)
    return l
