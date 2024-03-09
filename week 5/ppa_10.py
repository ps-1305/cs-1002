def insert(L, x):
    """
    insert an element x into a sorted list L

    Arguments:
        L: list
        x: integers
    Return:
        sorted_L: list
    """
    L.append(x)
    L = L.sort()
    return L
