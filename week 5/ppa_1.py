def factorial(n):
    """
    computes the factorial of an integer
    
    Argument:
        n: integer
    Return:
        result: integer
    """
    if n < 0:
        return -1
        
    if n == 1 or n == 0:
        return 1

    return n * factorial(n-1)

