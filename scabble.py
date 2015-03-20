def hawaiian_scrabble_score(my_string):
	#first check if it is a scrabble workd
	# if in list of letters
	#if not in list return -1
	#create dictionary of letters, string, with their corresponding point value
	h_dictionary = {'A':1,'K':2, 'O':2, 'I':3, 'N':3, 'E':4, "U":5, 'H':6, 'L':7, 'M':8, "P":8, 'W':9}
	score = 0
	for i in range(len(my_string)):
		if my_string[i] not in h_dictionary:
			return -1
		else:
			score = score + h_dictionary[my_string[i]]
	return score

print hawaiian_scrabble_score("PYTHON")