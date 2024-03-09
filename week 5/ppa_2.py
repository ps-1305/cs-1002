def check_leap_year(year):
    """
    check if the year is a leap year or not

    Argument:
        year: integer
    Return:
        is_leap_year: bool
    """
    if (1600 < year < 9999) and (year % 100 == 0) and (year % 400 == 0):
        return True

    if (1600 < year < 9999) and (year % 100 != 0) and (year % 4 == 0):
        return True
    
    return False 
