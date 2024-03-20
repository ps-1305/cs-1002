def ancestry(P, present, past):
    """
    A recursive function to compute the sequence of ancestors of person

    Arguments:
        P: dict, key and value are strings
        present: string
        past: string
    Return:
        result: list of strings
    """
    l = []
    if P[present] == past:
        l.append(present)
        l.append(past)
        return l
    else:
        l.append(present)
        pre = P[present] 
        pas = past
        return l + ancestry(P, pre, pas)
