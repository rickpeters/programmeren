def is_even(num):
    ''' (int) -> bool

    Return whether num is even.

    >>> is_even(4)
    True
    >>> is_even(77)
    False
    '''

    # variant 1: volledig uitgewerkt
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False

    # variant 2: expressie is al een boolean
    return num % 2 == 0
