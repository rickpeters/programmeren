def collect_vowels(s):
    """ (str) -> str

    Return the vowels from s. Do not treat the letter
    y as vowel.
    
    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('')
    ''
    """

    vowels = ''

    for char in s:
        if char.lower() in 'aeiou':
            vowels = vowels + char

    return vowels

def count_vowels(s):
    """ str) -> int

    Return the number of vowels in s. Do not treat the
    letter y as a vowel.

    >>> count_vowels('Happy Anniversary!')
    5
    >>> count_vowels('xyz')
    0
    """

    num_vowels = 0

    for char in s.lower():
        if char in 'aeiou':
            num_vowels = num_vowels + 1
            
    return num_vowels

    
