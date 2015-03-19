""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

digits = load_digits()
data = load_digits()
print data.DESCR
num_trials = 10
train_percentages = range(5,95,5)
test_accuracies = numpy.zeros(len(train_percentages))

fig = plt.figure()
for i in range(10):
	subplot = fig.add_subplot(5,2,i+1)
	subplot.matshow(numpy.reshape(digits.data[i],(8,8)),cmap='gray')

plt.show	
	

# train a model with training percentages between 5 and 90 (see train_percentages) and evaluate
# the resultant accuracy.
# You should repeat each training percentage num_trials times to smooth out variability
# for consistency with the previous example use model = LogisticRegression(C=10**-10) for your learner

# TODO: your code here


for size in train_percentages:
	total_accuracy = 0
	for i in range(0, num_trials):
		X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size = size)
		model = LogisticRegression(C=10**-10)
		model.fit(X_train,y_train)
		total_accuracy += model.score(X_test, y_test)
	test_accuracies[size/5.0-1] = total_accuracy/float(num_trials)
	# print size
	# print "Train accuracy %f" %model.score(X_train,y_train)
	# print "Test accuracy %f" %model.score(X_test, y_test)

fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()
