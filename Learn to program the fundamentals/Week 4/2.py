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
    """ (str) -> bool

    The parameter, dna is a potential DNA sequence. Return True if and only if the DNA sequence is valid (contains letters only 'A', 'G', 'C' or 'T'. A string is not a valid DNA sequence if it contains lowercase letters. 

    >>> is_valid_sequence('AAGCTTA')
    True
    >>> is_valid_sequence('AaGC')
    False
    >>> is_valid_sequence('ABCD')
    False
    """
    for c in dna:
        if c not in 'ATCG' or c.islower():
            return False
    return True
    
def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    The first two parameters are DNA sequences and the third parameter is an index. Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    """
    return dna1[:index] + dna2 + dna1[index:]
    
def get_complement(nuct,):
    """ (str) -> str

    The first parameter is a nucleotide. Return the nucleotide's complement.
    
    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    """
    
    if nuct == 'A':
        return 'T'
    elif nuct == 'T':
        return 'A'
    elif nuct == 'C':
        return 'G'
    elif nuct == 'G':
        return 'C'

def get_complementary_sequence(dna):
    """ (str) -> str

    The parameter is a DNA sequence. Return the DNA sequence that is complementary to the given DNA sequence.
    
    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CGACATTC')
    'GCTGTAAG'
    """
    comp_dna = ''
    for c in dna:
        comp_dna += get_complement(c)
    return comp_dna