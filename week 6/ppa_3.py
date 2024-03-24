def is_key(D, key):
    for i in D.keys():
        if i == key:
            return True
    return False

def value(D, key):
    for i in D.keys():
        if i == key:
            return D[key]
    return None
