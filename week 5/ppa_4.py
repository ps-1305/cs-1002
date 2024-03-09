def dim_equal(A, B):
    """
    check for dimensional equality of two matrices
    
    Arguments:
        A, B: list of lists
    Return:
        result: bool
    """
    return (len(A[0]) == len(B[0])) and (len(A) == len(B))
