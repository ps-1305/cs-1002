min=max=None
def get_range(L):
    """
    compute the range of a list L

    Parameters:
        L: list
    Return:
        range: float
    """
    maximum = minimum = L[0]
    for i in L:
        if i>maximum:
            maximum = i
        if i<minimum:
            minimum = i
    range = maximum-minimum
    return range
