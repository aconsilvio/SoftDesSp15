"""working with python classes"""

import copy 

#social networking groundwork

def my_function():
	"""some fucntion"""
	pass

class Person(object):
	"""representation of a person"""
	def __init__(self,first_name, last_name, job, height):
		self.first_name = first_name
		self.last_name = last_name
		self.job = job
		self.height = height

	def add_friend(self,friend):
		self.friends.append(friend)

	def __str__(self):
		"""Prints out person's attributes
		>>>print_person(annabel)
		Annabel is the coolest person"""
		templete = "{first} {last} is {job}"
		return templete.format(first = self.first_name, last = self.last_name, job = self.job)


#Create a new annabel Person and assign her attributes
annabel = Person("Annabel","Consilvio","the coolest person", [5,2])
annabel.first_name = "Annabel"
annabel.last_name = "Consilvio"
annabel.job = 'the coolest person'
annabel.height = [5,2]

print annabel

#Create some more people
#paul = Person()
#paul.first_name = "Paul"
#paul.last_name = "Ruvolo"
#paul.job = "Professor"
#paul.height = [6,2]

#blinder = copy.deepcopy(paul)
#blinder.last_name = "Linder"
#blinder.first_name = "Ben"

if __name__ == '__main__':
    import doctest
    doctest.testmod()
#blinder.print_person()
#paul.print_person()