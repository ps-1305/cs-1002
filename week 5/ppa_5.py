def first_three(L):
    '''
    find the first three maximums in the list
    Argument:
        L: list of ints
    Return:
        (fmax, smax, tmax): (int, int, int)
    '''
    # you can use any sorting algorithm, I went with time complexity of n^2
    L = sorted(L)
    return (L[len(L)-1], L[len(L)-2], L[len(L)-3])
