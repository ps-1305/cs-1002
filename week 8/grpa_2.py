def linear(P, Q, k):
    """
    A recursive function to determine if a list is scalar multiple of the other

    Arguments:
        P: list of integers
        Q: list of integers
        k: integer
    Return:
        result: bool
    """
    if(len(P) == 1 and len(Q) == 1 and P[0] == k * Q[0]):
        return True
    if(len(P) != len(Q)):
        return False
    if(P[-1] != k * Q[-1]):
        return False
    if(len(P) == len(Q) and P[-1] == k * Q[-1]):
        P.pop()
        Q.pop()
        return linear(P,Q,k)
    
