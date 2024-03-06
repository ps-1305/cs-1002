def distance(word_1, word_2):
    """
    compute distance between words

    Parameters:
        word_1: str
        word_2: str
    Return:
        dist: int
    """
    dist = 0
    if len(word_1) != len(word_2):
        return -1
    for i in range(len(word_1)):
        dist += abs(ord(word_1[i])-ord(word_2[i]))
    return dist
