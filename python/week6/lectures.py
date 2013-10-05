def count_matches(s1, s2):

    num_matches = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1
    return num_matches

def averages(grades):
    """
    list of list of number) -> list of float

    Precondition: grades contains at least one element with one grade

    Return a list of averages for each list of individual grades in list grades
    
    >>> averages([[70, 75, 80], [70,80,90,100], [80,100]])
    [75.0, 85.0, 90.0]
    """

    averages = []
    for grades_list in grades:
        # calculate the acerage of grades_list and append it
        # to averages

        total = 0
        for mark in grades_list:
            total = total + mark

        averages.append(total / len(grades_list))

    return averages
