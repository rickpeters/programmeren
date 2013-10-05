def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    
    num_letters = 0

    for char in dna:
        if char in 'agctAGCT':
            num_letters = num_letters + 1

    return num_letters


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
    return dna.count(nucleotide)

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
    """(str) -> bool

    returns if it is a dna string or not.

    >>> is_valid_sequence('TGCTA')
    True
    >>> is_valid_sequence('TAQWIU')
    False

    """
    dna_test = True

    for char in dna:
        if not char in 'AGTC':
            dna_test = False

    return dna_test

def insert_sequence(dna1, dna2, num):
    """(str, str, int) -> str

    Places the dna2 in dns1 on the spot you give.

    >>> insert_sequence('AAAA', 'CC', 3)
    'AAACCA'
    >>> insert_sequence('ACCTG', 'AC', 2)
    'ACACCTG'

    """

    return dna1[:num] + dna2 + dna1[num:]

def get_complement(nuc):
    """(str) -> str

    Gives the complement of the nuc (nucleotide).

    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    """

    comp = ''

    if nuc == 'A':
        comp = 'T'
    if nuc == 'T':
        comp = 'A'
    if nuc == 'C':
        comp = 'G'
    if nuc == 'G':
        comp = 'C'

    return comp

def get_complementary_sequence(dna):
    """(str) -> str

    returns the complement of the dna sequence.

    >>> get_complementary_sequence('AATTCCGG')
    'TTAAGGCC'
    >>> get_complementary_sequence('AAGG')
    'TTCC'
    >>> get_complementary_sequence('TAGCTAGC')
    'ATCGATCG'
    >>> get_complementary_sequence('AT')
    'TA'
    """

    comp_dna = ''
    
    for char in dna:        
        comp_dna = comp_dna + get_complement(char)

    return comp_dna
