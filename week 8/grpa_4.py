def steps(n):
    """
    A recursive function to compute the number of ways to ascend steps 

    Argument:
        n: integer
    Return:
        result: integer
    """
    if(n<4):
        initial = [1,2,4]
        return initial[n-1]
    else:
        return steps(n-1) + steps(n-2) + steps(n-3)
