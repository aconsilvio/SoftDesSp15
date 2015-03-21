""" 
Exploring learning curves for classification of handwritten digits 
By Annabel Consilvio
"""

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

#starter code
data = load_digits()
print data.DESCR
num_trials = 10
train_percentages = range(5,95,5)
test_accuracies = numpy.zeros(len(train_percentages))
average_list = []  #initalizes empty list
for i in range(len(train_percentages)):  #loops through precentages
	for test in range(num_trials): #repeats function for specified number of trials
		X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size= train_percentages[i]*0.01)
		model = LogisticRegression(C=10**-15)
		model.fit(X_train, y_train)
		average_list.append(model.score(X_test,y_test)) #appends accuracy of test to list
	test_accuracies[i] = sum(average_list)/ float(num_trials) #finds average of list and replaces corresponding element in list


#plotting code
fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()