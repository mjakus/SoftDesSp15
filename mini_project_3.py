""" search twitter for trending topics, calculate average subjectivity and sentiment
 about each trending topic

 Maggie Jakus, 2/25/15
"""
from pattern.web import Bing, SEARCH, plaintext, Twitter
from pattern.en import sentiment
from pattern.search import search
import string
import time
import matplotlib.pyplot as plt
import numpy as np

def trending_topics():
	topics = Twitter().trends(cached=False) # gets the trending topics from twitter
	return topics  # as a list


engine = Bing(license = 'A/GIVHcrjHaE/o45RWe8rkbOmqxeoRwwhwcHY2zHE34')
def search_bing(trending_topics): # takes in a list of topics to search
	input_data = dict() # make a dictionary
	for topic in trending_topics: # for each trending topic
		vals_for_dict = [] # the values for a particular topic, will be a list of strings
		for i in range(1,10): 
			for result in engine.search(topic, type = SEARCH, start = i): # for each result for that topic
				vals_for_dict.append([repr(plaintext(result.text))]) # append the results to a list of the results for that topic
		input_data[topic] = vals_for_dict # return a dictionary that has that topic as a key and a list of all results as the value
	# print input_data
	return input_data # dictionary of twitter topics and lists of bing results for those topics

def analyze_bing(data): #data is a dictionary of topics (keys) and the corresponding bing search results (values)
	topic_polarity_subjectivity = dict() # dictionary to be returned, contains topic (the key) and polarity, subject as tuple (the value)
	for topic in data: # each topic from twitter
		polarity = 0 #the polarity/ sentiment of the statement
		subjectivity = 0 #how subjective the statement is
		number = 0 #counter for number of titles run through
		value = data[topic]
		for bing_search in value: # sentence of the list, which is in and of itself a list
			# print "bing_search:", bing_search
			for content in bing_search:
				polar, subject = sentiment(content) # calculates polarity and subjectivity of that particular result
				polarity += polar
				# print "polarity:", polarity
				subjectivity += subject
				number += 1 # needed to calculate average subjectivity and polarity of bing results for the given Twitter topic
		if number != 0:
			topic_polarity_subjectivity[topic] = (polarity/float(number), subjectivity/float(number))
		else:
			topic_polarity_subjectivity[topic] = (0.0,0.0)
	return topic_polarity_subjectivity

def compare_polarity(topic_polarity): # this takes in a dictionary of topic: (polarity, subjectivity) from analyze_bing
	num_of_columns = len(topic_polarity)
	n_groups = num_of_columns
	values = []
	labels = []
	for topics in topic_polarity:
		tuple1 = topic_polarity[topics]		
		polarity = tuple1[0]
		values.append(polarity)
		# name = topics
		labels.append(topics)

	index = np.arange(n_groups)
	bar_width = 0.35

	opacity = 0.6

	rects1 = plt.bar(index, values, bar_width,
	    alpha=opacity,
	    color='b')

	plt.title("Average Polarity of Bing Content of Twitter's Trending Topics")
	plt.xticks(index + bar_width, labels)
	plt.xlabel("Trending Topics")
	plt.ylabel("Polarity")

	plt.tight_layout()
	plt.show()


# test = {'cat': (1,2), 'dog': (4,5)}
# print compare_polarity(test)

# these give the actual results!
topics = trending_topics()
to_be_analyzed = search_bing(topics)
# print analyze_bing(to_be_analyzed)
print compare_polarity(analyze_bing(to_be_analyzed))
