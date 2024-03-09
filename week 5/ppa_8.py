def fibo(n):
    '''
    compute the nth fibonacci number

    Argument:
        n: int
    Return:
        result: int
    '''
    term1 , term2 = 0, 1
    next_term = 0
    for i in range(n-1):
        next_term = term1 + term2
        term1 = term2 
        term2 = next_term
    return next_term
        
