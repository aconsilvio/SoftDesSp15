def filter_out_negative_numbers(my_list):
	#create an if statement that determine if each element of the list is positive
	# if positive append it to a new list
	# if negative ignore
	new_list = []
	for i in range(len(my_list)):
		if my_list[i] >= 0:
			new_list.append(my_list[i])

	return new_list

#print filter_out_negative_numbers([-2.0, 5.0, 10.0, -100.0, 5.0])

def in_language(my_string):
	#make a function that splits the string in half?
	#then have it look at each element of each string 
	#check if all the elements of first strring are as
	#check if all the elements of first string are bs
	#then return true or false
	halfpoint = len(my_string)/2
	firsthalf = my_string[:halfpoint]
	secondhalf = my_string[halfpoint:]
	for i in range(halfpoint):
		if firsthalf[i] == 'a' and secondhalf[i]== 'b':
			return True
		else:
			return False

print in_language('aaaabbbb')