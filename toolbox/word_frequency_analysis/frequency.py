""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THE PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]
	punct = string.punctuation

	no_punct = ""
	for line_current in lines:
		for element in line_current:
			if element not in punct:
				no_punct = no_punct + element

	book_nopunc_space = no_punct.split()

	book_final = [element.lower() for element in book_nopunc_space]

	return book_final

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	dictionary = {}
	for element in word_list:
		if element in dictionary:
			dictionary[element] = dictionary[element] + 1
		else:
			dictionary[element] = 1
	
	ordered_by_frequency = sorted(dictionary, key=dictionary.get, reverse=True)
	return ordered_by_frequency[:n]

final_words = get_word_list("pride.txt")

get_top_n_words(final_words,100)