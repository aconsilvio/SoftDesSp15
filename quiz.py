"""quiz 3/9/15"""
import copy

class DNASequence(object):
    """ Represents a sequence of DNA """
    def __init__(self, nucleotides):
        """ constructs a DNASequence with the specified nucleotides.
             nucleotides: the nucleotides represented as a string of
                          capital letters consisting of A's, C's, G's, and T's """
        self.nucelotides = nucleotides
 
    def __str__(self):
        """ Returns a string containing the nucleotides in the DNASequence
        >>> seq = DNASequence("TTTGCC")
        >>> print seq
        TTTGCC
        """
        template = "{sequence}"
       	return template.format(sequence = self.nucleotides)


    def get_reverse_complement(self):
        """ Returns the reverse complement DNA sequence represented
            as an object of type DNASequence
            >>> seq = DNASequence("ATGC")
            >>> rev = seq.get_reverse_complement()
            >>> print rev
            GCAT
            >>> print type(rev)
            <class '__main__.DNASequence'>
        """
        complement_dict = {'A':'T', 'T':'A', 'C':'G','G':'C'}
        complement_string = ''
        reverse_complement = ''
        complement = ''
        for letter in self.nucleotides:
			complement = complement_dict.get(letter)
			complement_string = complement_string + complement
		for letter in range(len(complement_string)):
			reverse_complement = reverse_complement + complement[len(complement_string)-1-letter]
		return reverse_complement




    def get_proportion_ACGT(self):
        """ Computes the proportion of nucleotides in the DNA sequence
            that are 'A', 'C', 'G', and 'T'
            returns: a dictionary where each key is a nucleotide and the
                corresponding value is the proportion of nucleotides in the
            DNA sequence that are that nucleotide.
            (NOTE: this doctest will not necessarily always pass due to key
                    re-ordering don't worry about matching the order)
        >>> seq = DNASequence("AAGAGCGCTA")
        >>> d = seq.get_proportion_ACGT()
        >>> print (d['A'], d['C'], d['G'], d['T'])
        (0.4, 0.2, 0.3, 0.1)
        """
        #for letter in self.nucleotides:
        letter_dict = {'A':0, 'T':0, 'C':0,'G':0}
        for letter in self.nucleotides:
        	if letter == 'A':
        		letter_dict['A'] = letter_dict.get('A') + 1
        	elif letter == ['T']:
        		letter_dict['T'] = letter_dict.get('T') + 1
        	elif letter == ['C']:
        		letter_dict['C'] = letter_dict.get('C') + 1
        	elif letter == ['G']:
        		letter_dict['G'] = letter_dict.get('G') + 1
        tot_num = len(self.nucleotides)
        for element in letter_dict:
        	letter_dict[element] = letter_dict.get(element) / tot_num
        return letter_dict



if __name__ == '__main__':
    import doctest
    doctest.testmod()