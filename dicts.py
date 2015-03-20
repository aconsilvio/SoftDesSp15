"""hey hey hey we're learning about dictionaries"""

d = {"banana" : 0}

d["apple"]= 2

#print "apple" in d


def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

#print histogram('hello')

def histogram2(s):
	d = dict()
	for letter in s:
		d[letter] = d.get(letter,0) + 1 
	return d

#print histogram2("hello")

def reverse_lookup(d,v):
	listt = []
	for k in d:
		if d[k] == v:
			listt.append(k)
	return listt
	raise ValueError

h = histogram2("parrotsareawesome")
print reverse_lookup(h,3)


"""lists and dictionaries"""

###DONT USE LISTS AS KEYS IN dictionaries

def fibbo(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibbo(n-1) + fibbo(n-2)