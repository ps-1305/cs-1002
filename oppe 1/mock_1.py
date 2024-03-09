def primes(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def twin_primes(p, q):
    '''
    Determine if p and q are twin primes
    
    Parameters:
    	p: int
    	q: int
    Return:
    	result: bool
    '''
    return primes(p) and primes(q) and (abs(p-q) == 2)
