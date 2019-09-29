def haming_metric(father, child):
    distance = 0
    zipped_dna = zip(father, child)
    for pair in zipped_dna:
        if pair[0] != pair[1]:
            distance += 1
    return distance



if __name__ == '__main__':
    first_candidate = input('first candidate DNA: ')
    second_candidate = input('second candidate DNA: ')
    child_pattern = input('child DNA: ')
    first_father = haming_metric(first_candidate, child_pattern)
    second_father = haming_metric(second_candidate, child_pattern)
    if first_father < second_father:
        print('first candidate is a father')
    else:
        print('second candidate is a father')