def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for each in dna:
        if nucleotide == each:
            count+=1
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
    lst = ['A', 'C', 'T', 'G', '']
    flag = True
    for each in dna:
        if each in lst:
            flag = True
        else:
            flag = False
    return flag


def insert_sequence(dna1, dna2, index):
    temp = dna1[:index]
    rest = dna1[index:]
    return temp+dna2+rest
        
def get_complement(nucleotide):
    compliment = {'A': 'T', 'T':"A", 'C':"G", 'G':"C"}
    return compliment[nucleotide]

def get_complementary_sequence(dna):
    final  = ""
    for each in dna:
        final += get_complement(each)
    return final
