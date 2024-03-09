# mysterious is a function given to us
def type_of_sequence(words):
    '''
    Find the type of the list based on its contents

    Argument:
        words: list of strings
    Return:
        list_type: string
    
    '''
    k = 0
    for i in range(len(words)):
        if mysterious(words[i]):
            k += 1
    if k < 2:
        return "mildly mysterious"
    elif 2 < k < 5:
        return "moderately mysterious"
    else:
        return "most mysterious"
