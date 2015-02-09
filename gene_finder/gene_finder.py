# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Annabel Consilvio

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq
dna = load_seq("./data/X73525.fa")

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    """
    #if statements change nucleotide inputs to their complementary nucleotide
    if nucleotide == "A":
        return "T"
    if nucleotide == "T":
        return "A" 
    if nucleotide == "C":
        return "G"
    if nucleotide == "G":
        return "C"         


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    >>> get_reverse_complement('ATGTGTGTGCCCAA')
    'TTGGGCACACACAT'
    """
    #set up initial empty strings for later use
    complement = ""
    reverse_complement = ""

    #for each element in the list of dna, get the complement and add it to an empty list
    for i in range(len(dna)):
        complement = complement + get_complement(dna[i]) 

    #for each element in the list of complement, return the complement by calling the list in reverse
    for i in range(len(dna)):
        reverse_complement = reverse_complement + complement[len(dna)-1-i]

    return reverse_complement 



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
    >>> rest_of_ORF("ATGGGGGGCCCCTAG")
    'ATGGGGGGCCCC'
    """

    #inital conditions
    i = 3
    end_index = len(dna)
    stop_codon = ('TAG','TAA','TGA')

    #for the length of the string of DNA, run through each codon and break and return the indec of the string if the codon is a stop codon
    while i < len(dna)-2:
        codon = dna[i:i+3] #takes only every third index which is the length of a codon
        if codon in stop_codon:
            end_index = i         
            break
        i += 3
    #returns a list from the start codon to the index where the stop codon begins
    return dna[0:end_index]
    



def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    >>> find_all_ORFs_oneframe("ATGCCATGTTATGAATAG")
    ['ATGCCATGTTATGAA']
    """
    #inital conditions
    i = 0
    start_codon = ('ATG')
    end_index = len(dna)
    return_variable = []

    #for each codon in the set of DNA, check if it is a start codon
    #if it is a start codon, add the string until the stop codon to a list
    #then continue running
    while i < len(dna)-2:
        codon = dna[i:i+3]    
        if codon in start_codon:
            orf = rest_of_ORF(dna[i:])
            return_variable.append(orf)
            i += len(orf)
        i += 3


    #return a list of strings of DNA
    return return_variable
    

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    >>> find_all_ORFs("ATGTTTTATGTAG")
    ['ATGTTTTATGTAG', 'ATG']
    """
    #inital conditions
    i = 0
    start_codon = ('ATG')
    end_index = len(dna)
    return_variable = []

    #for statement tells the code to run three times at three inital index values
    #0,1,and 2 which allows for each reading frame to be read
    for i in range (3):
        while i < (len(dna)-2):
            codon = dna[i:i+3]    
            if codon in start_codon: #check if the codon the code is looking at is a start codon
                orf = rest_of_ORF(dna[i:]) #then determine that this is an orf, make it a string given the index of the start codon
                return_variable.append(orf) #and append said string to a list of ORFs
                i += len(orf) 
            i += 3
    #return a list of strings of DNA from both strands
    return return_variable


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    >>> find_all_ORFs_both_strands("ATGTGGAT")
    ['ATGTGGAT']

    """
    #inital conditions
    all_of_them = []

    #compute the all of the orfs in a DNA strand and the find their reverse complements
    #the return both of them in a list that includes all of the ORFS on both strands
    normal_ORFs = find_all_ORFs(dna)
    reverse_complement = get_reverse_complement(dna)
    reverse_ORFs = find_all_ORFs(reverse_complement)
    all_of_them = normal_ORFs + reverse_ORFs
    return all_of_them



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    >>> longest_ORF("ATGGGGGGCCCC")
    'ATGGGGGGCCCC'
    """
    '''
    lengths = []
    list_of_orfs = find_all_ORFs_both_strands(dna)

    number_of_orf = len(list_of_orfs)
    
    for i in range (0, number_of_orf):
        print 'IM IN THE LOOP!!!!!!!!!!!'
        length = len(list_of_orfs[i])
        lengths.append(length)
    print lengths

    max_value = max(lengths)

    index_max = lengths.index(max_value)
    #need to get get the index number of the max of the list


    return list_of_orfs[index_max]'''



    #use the find_all_orfs_both_strands function and then compute the max length of these
    ORFs = find_all_ORFs_both_strands(dna)
    return max(ORFs,key=len)



def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF         
        """
    #inital conditions
    lengths = []

    #shuffle the strand of DNA and then look for the longest ORF within the randomly shuffled strand
    for i in range (0,num_trials):
        shuffle = shuffle_string(dna)
        length = len(longest_ORF(shuffle))
        lengths.append(length)

    #determine the orf with the longest length and return it
    max_value = max(lengths)


    return max_value





    

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
        >>> coding_strand_to_AA("ATGCCCGCTTTCCCAAA")
        'MPAFP'
    """
    #inital conditions
    protein = ''
    i = 0

    #for the length of DNA, translate each codon in an ORF to an amino acid
    while i < (len(dna)-2):
        codon = dna[i:i+3]    
        amino_acid = aa_table[codon]
        protein= protein + amino_acid
        i += 3

    #return the string of amino acids
    return protein


def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.

    """
    #use longest_ORF_noncoding to determine what the longest strand of DNA could be in a random sequence
    threshold = longest_ORF_noncoding(dna,1500)

    #find all of the orfs on both strand and the generate an empty list
    all_orfs = find_all_ORFs_both_strands(dna)
    all_orfs_long = []

    #this makes a list of strings of dna that are longer than the threshold

    for i in range (0, len(all_orfs)):
        if len(all_orfs[i]) > threshold:
            all_orfs_long.append(all_orfs[i])

    #this takes each dna string in a list and converts it to an amino acid sequence

    aa_list = []

    for i in range (0, len(all_orfs_long)):
        aa_strand = coding_strand_to_AA(all_orfs_long[i])
        aa_list.append(aa_strand)

    #returns strings of amino acids
    return aa_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#print get_complement('A')
#print get_complement('C')
#print get_reverse_complement('ATGCGGT')
#print rest_of_ORF("ATGAGATAGG")
#print find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
#print find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
#print gene_finder(dna,1)
#print longest_ORF_noncoding("ATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAA",100)
#print gene_finder('CCTATCAACTAAAATGTTGAAGTATGAAGAGCGGAAGCTGAATAATCTGACCTTGTCGTCGTTCTCCAAGGTCGGTGTTTCAAACGATGCTAGATTGTATATTGCCAAAGAAAACACTGACAAGGCATACGTCGCGCCGGAAAAGTTTTCAAGCAAAGTCCTCACCTGGCTCGGTAAGATGCCTCTTTTTAAGAATACAGAGGTCGTCCAAAAACATACTGAAAACATACGAGTCCAAGATCAGAAAATTTTGCAGACTTTCCTACATGCTCTTACTGAGAAATACGGGGAGACTGCTGTGAACGACGCACTACTAATGTCCCGGATAAATATGAACAAACCACTCACACAAAGGTTGGCCGTTCAGATAACTGAGTGTGTAAAAGCCGCCGATGAGGGCTTCATCAACCTAATCAAGAGCAAGGACAACGTCGGAGTAAGAAACGCTGCCTTAGTAATTAAGGGTGGGGATACTAAAGTGGCGGAAAAAAACAACGACGTCGGGGCAGAGTCCAAGCAACCTCTTTTAGATATAGCACTGAAGGGTCTGAAGAGGACACTCCCTCAATTAGAGCAGATGGACGGGAATAGTCTAAGGGAAAACTTTCAAGAAATGGCTTCCGGCAATGGGCCTCTCCGTTCCTTGATGACGAATCTGCAGAACTTAAATAAGATTCCTGAGGCTAAACAGTTAAACGACTACGTTACGACCTTAACAAATATACAAGTAGGTGTCGCGCGCTTTAGTCAATGGGGCACATGTGGGGGAGAGGTCGAACGCTGGGTAGATAAAGCTAGTACCCACGAGCTCACCCAAGCAGTCAAAAAGATCCATGTGATTGCGAAGGAACTAAAGAACGTTACTGCTGAATTGGAAAAAATCGAGGCAGGGGCGCCGATGCCGCAAACAATGTCGGGTCCCACGTTAGGTCTGGCACGGTTCGCGGTCAGCTCAATACCCATCAACCAGCAAACCCAAGTCAAATTATCGGACGGGATGCCAGTTCCCGTTAATACATTAACCTTCGACGGGAAACCCGTGGCACTGGCTGGGAGCTACCCTAAGAACACTCCCGACGCACTGGAGGCTCACATGAAGATGCTGCTCGAAAAGGAATGCTCGTGCCTGGTAGTTCTTACGTCAGAAGATCAGATGCAAGCCAAGCAATTGCCACCGTACTTTCGTGGGAGCTACACCTTCGGTGAGGTGCACACCAATTCACAGAAGGTGTCATCTGCATCGCAAGGGGAGGCCATTGATCAGTACAATATGCAGTTATCCTGCGGCGAGAAAAGGTACACCATACCCGTACTCCACGTAAAAAACTGGCCCGATCATCAGCCCCTCCCGAGTACGGATCAACTCGAATATTTGGCAGACAGGGTAAAAAATAGCAATCAAAATGGTGCCCCCGGACGCTCCTCTTCGGATAAGCACCTGCCAATGATTCATTGCCTGGGAGGCGTCGGAAGAACGGGAACCATGGCAGCGGCCCTGGTCTTAAAGGACAATCCGCACAGTAATCTAGAGCAGGTGCGAGCAGATTTCAGAGATTCTCGTAACAACCGCATGTTGGAAGATGCATCCCAGTTCGTTCAGTTGAAGGCGATGCAAGCGCAACTTCTGATGACTACTGCGAGCTGATGGCCCCGGTGTATGCCAGTAC',1)