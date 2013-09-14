def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    length = 0

    for char in dna:
        length = length + 1

    return length

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    count = 0

    for char in dna:
        if char == nucleotide:
            count = count + 1

    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    return True if and only if all chars in dna are DNA nucleotides (A, T, C and G, uppercase only)

    >>> is_valid_sequence('ATCG')
    True
    >>> is_valid_sequence('ATcG')
    False
    >>> is_valid_sequence('')
    True
    >>> is_valid_sequence('wrong')
    False

    """

    for char in dna:
        if not char in 'ATCG':
            return False

    return True

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    return a new sequence where dna2 is insert at dna1 at position index

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('', 'ATC', 0)
    'ATC'
    >>> insert_sequence('CCGG', 'AT', 4)
    'CCGGAT'
    >>> insert_sequence('CCGG', 'AT', 0)
    'ATCCGG'
    """

    dna3 = dna1[:index] + dna2 + dna1[index:]

    return dna3

def get_complement(nucleotide):
    """ (str) -> str

    return the complement of nucleotide, where the complement of A = T and the complement of C = G

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """

    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'

def get_complementary_sequence(dna):
    """ (str) -> str

    return the complementary sequence for dna

    >>> get_complementary_sequence('ATGC')
    'TACG'
    >>> get_complementary_sequence('AAGGC')
    'TTCCG'
    """

    dna2 = ''

    for char in dna:
        dna2 = dna2 + get_complement(char)

    return dna2