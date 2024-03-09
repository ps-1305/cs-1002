# f1 = f2 = 1 are the first two fibonacci numbers
def fibo(n):
    '''
    compute the nth fibonacci number

    Argument:
        n: int
    Return:
        result: int
    '''
    term1 , term2 = 1, 1
    if n == 1 or n == 2:
        return term1
    for i in range(n-2):
        next_term = term1 + term2
        term1 = term2 
        term2 = next_term
    return next_term
        
