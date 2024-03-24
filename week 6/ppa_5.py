def dict_to_list(D):
    l = []
    for i in D.keys():
        l.append(tuple([i,D[i]]))
    return l
def list_to_dict(L):
    d = dict()
    for i in L:
        d[i[0]] = i[1]
    return d
