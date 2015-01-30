# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """
    takes in a nucleotide, returns the complement nucleotide

    I added this because there was no unit test for this function. I wanted to test more than just one case.
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'

    pass

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string

        I don't think this needs any more unit tests. It seems to work and there aren't 
        any other noticeably different tests.
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    complement = ''
    for  i in range(len(dna)):
        complement = complement + get_complement(dna[i])
    reverse_comp = ''
    for i in range(len(dna)):
        reverse_comp = reverse_comp + complement[len(dna)-1-i]

    return reverse_comp

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'

    I added this to test if it will run properly when the stop codon is not in sequence
    >>> rest_of_ORF('ATGATAG')
    'ATGATAG'
    """
    stop_codons = ('TAG','TAA','TGA')
    end_index = len(dna)
    i = 3
    while i < (len(dna)-2):
        codon = dna[i:i+3]
        if codon in stop_codons:
            end_index = i
            return dna[0:end_index]
        i += 3
    return dna


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

        I don't think this needs any other tests. The unit test is very long and thorough.
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    # TODO: implement this
    start = 'ATG'
    i = 0
    end_index = len(dna)
    return_variable = []
    while i < (len(dna)-2):
        codon = dna[i:i+3]
        if codon == start:
            orf = rest_of_ORF(dna[i:])
            return_variable.append(orf)
            i += len(orf)
        i+=3
    return return_variable

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        dna: a DNA sequence
        returns: a list of non-nested ORFs

        I don't think this needs any other tests. The unit test is very long and thorough.
    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    start = 'ATG'
    stop_codons = ('TAG','TAA','TGA')
    end_index = len(dna)
    all_orfs = []
    for i in range(3):
        while i < (len(dna)-2):
            codon = dna[i:i+3]
            if codon == start:
                orf = rest_of_ORF(dna[i:])
                all_orfs.append(orf)
                i+=len(orf)
            i+=3
    return all_orfs

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
        I don't think this needs any other tests. The unit test is very long and thorough.
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    actually_all_of_them = []
    normal_ORFS = find_all_ORFs(dna)
    reverse_complement = get_reverse_complement(dna)
    reverse_ORFS = find_all_ORFs(reverse_complement)
    actually_all_of_them = normal_ORFS + reverse_ORFS
    return actually_all_of_them



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    pass


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    pass

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    pass

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # TODO: implement this
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()

print get_complement('C')
print get_reverse_complement('CAT')
print rest_of_ORF('ATGAAATAA')
print find_all_ORFs_oneframe('ATGCATGAATGTAGATAGATGTGCCC')
print find_all_ORFs("ATGCATGAATGTAG")
print find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")