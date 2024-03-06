def is_perfect(num):
    """
    determine if a number is perfect or not

    Parameters:
        num: int
    Return:
        result: bool
    """
    divisors = 0
    for i in range(1, num):
        if num%i == 0:
            divisors += i
    if divisors == num:
        return True
    return False
    
print(is_perfect(int(input())))
