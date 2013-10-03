def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:     # <--- How many times is this line reached?
            matches = matches + 1
    
    return matches == (len(s) // 2)

def shift_right(L):
    """ (list) -> NoneType

    Shift each item in L one position to the right
    and shift the last item to the first position.

    Precondition: len(L) >= 1
    """

    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]
        
    L[0] = last_item

def make_pairs(list1, list2):
    """ (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with the string from the
    corresponding position of list1 and the int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    """
    
    pairs = []
    
    # CODE MISSING HERE
    # alternatief 1
    for i in range(len(list1)):
       inner_list = []
       inner_list.append(list1[i])
       inner_list.append(list2[i])
       pairs.append(inner_list)
    # alternatief 2
    #for i in range(len(list1)):
    #       pairs.append([list1[i], list2[i]])      

    return pairs

def contains(value, lst):
    """ (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    """

    found = False  # We have not yet found value in the list.

    # CODE MISSING HERE
    # alternatief 1
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True

    # alternatief 2
    #for sublist in lst:
    #    if value in sublist:
    #        found = True

    return found

def print_file(str):
    # data_file refers to a file open for reading.
    data_file = open(str, 'r')
    for line in data_file:
        print(line.rstrip('\n'))

    data_file.close()

def lines_startswith(file, letter):
    """ (filename, str) -> list of str

    Return the list of lines from file that begin with letter. The lines should have the
    newline removed.

    Precondition: len(letter) == 1
    """

    data_file = open(file, 'r')

    matches = []

    # alternatief 1
    for line in data_file:
        #print(line)
        if letter == line[0]:
            print(line)
            matches.append(line.rstrip('\n'))
            
    data_file.close()

def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """
    data_file = open(file, 'w')

    # CODE MISSING HERE
    for s in sentences:
        data_file.write(s)    
    data_file.close()
