# work file for exam course python programming
def count_max_letters(s1, s2, letter):
    """(str, str, str) -> int

    s1 and s2 are strings, and letter is a string of length 1.  Count how many
    times letter appears in s1 and in s2, and return the bigger of the two
    counts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    """

    return max(s1.count(letter), s2.count(letter))

def both_start_with(s1, s2, prefix):
    """(str, str, str) -> bool

    Return True if and only if s1 and s2 both start with the letters in prefix.
    """
    return s1.startswith(prefix) and s2.startswith(prefix)

def reverse(s):
    """(str) -> str

    Return the reverse of s.

    >>> reverse('abc')
    'cba'
    >>> reverse('a')
    'a'
    >>> reverse('madam')
    'madam'
    >>> reverse('1234!')
    '!4321'
    """

    result = ''
    i = len(s) - 1
    while i >= 0:
        result = result + s[i]
        i = i - 1

    return result


def get_keys(L, d):
    """(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    """

    result = []
    for k in d:
        if k in L:
            result.append(k)

    return result

def count_values_that_are_keys(d):
    """(dict) -> int

    Return the number of values in d that are also keys in d.

    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    """

    result = 0
    for k in d:
        if d[k] in d:
            result = result + 1

    return result

def double_last_value(L):
    """(list of int) -> NoneType

    Double the value at L[-1].  For example, if L[-1] is 3,
    replace it with 6.

    Precondition: len(L) >= 1.
    """
    L[-1] = L[-1] * 2

    
def get_negative_nonnegative_lists(L):
    """(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    """

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # variant 1, fout!
            #if L[row][col] > 0:
            #    nonneg.append(L[row][col])
            #else:
            #    neg.append(L[row][col])

            # variant 2, goed
            #if 0 <= L[row][col]:
            #    nonneg.append(L[row][col])
            #else:
            #    neg.append(L[row][col])

            #variant 3, goed
            #if L[row][col] < 0:
            #    neg.append(L[row][col])
            #else:
            #    nonneg.append(L[row][col])

            # variant 4, fout
            #if L[row][col] < 0:
            #    neg.append(L[row][col])
            #
            #nonneg.append(L[row][col])

            # variant 5, goed
            if L[row][col] > 0:
                nonneg.append(L[row][col])
            elif L[row][col] < 0:
                neg.append(L[row][col])
            else:
                nonneg.append(L[row][col])

    return (neg, nonneg)

def count_chars(s):
    """(str) -> dict of {str: int}

    Return a dictionary where the keys are the characters in s and the values
    are how many times those characters appear in s.

    >>> count_chars('abracadabra') ==  {'d': 1, 'c': 1, 'b': 2, 'a': 5, 'r': 2}
    True
    """

    # had to change the docstring to account for random ordering of keys in dict

    d = {}

    for c in s:
        if not (c in d):
            d[c] = 1
        else:
            d[c] = d[c] + 1

    return d