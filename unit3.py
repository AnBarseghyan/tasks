def odd_Tuples (aTup: tuple):
    '''

    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    bTup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            bTup = bTup + (aTup[i], )
    return bTup


print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))








