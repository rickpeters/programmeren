def count_matches(s1, s2):

    num_matches = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1
    return num_matches

