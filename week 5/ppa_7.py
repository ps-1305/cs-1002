def is_empty(L):
    '''
    check if the list is empty
    Argument:
        L: list
    Return:
        result: boolean
    '''
    if len(L):
        return True
    return False

def first(L):
    '''
    return the first element of the list
    Argument:
        L: list
    Return:
        result: int
    '''
    return L[0]

def last(L):
    '''
    return the last element of the list
    Argument:
        L: list
    Return:
        result: int
    '''
    return L[-1]

def init(L):
    '''
    return first n - 1 elements of the list
    Argument:
        L: list
    Return:
        result: list
    '''
    new = []
    for i in range(0, len(L)-1):
        new.append(L[i])
    return new

def rest(L):
    '''
    return the last n - 1 elements of the list
    Argument:
        L: list
    Return:
        result: list
    '''
    new = []
    for i in range(1,len(L)):
        new.append(L[i])
    return new

