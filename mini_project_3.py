# search twitter for trending topics, calculate average subjectivity and sentiment about each thing

from pattern.web import Bing, SEARCH, plaintext
from pattern.en import sentiment
from pattern.search import search
from pattern.web import Twitter
import string
import time

def trending_topics():
	topics = Twitter().trends(cached=False) # gets the trending topics from twitter
	return topics


engine = Bing(license = None)
def search_bing(trending_topics): # takes in a list of topics to search
	input_data = dict()
	vals_for_dict = []
	for topic in trending_topics: # for each trending topic
		for i in range(1,10): # do this 10 times
			# retry = True
			# while retry:
			# 	try:
			for result in engine.search(topic, type = SEARCH, start = i): # for each result for that topic
				vals_for_dict.append([repr(plaintext(result.text))]) # append the results to a list of the results for that topic
					retry = False
				except:
					time.sleep(5)
		input_data[topic] = vals_for_dict # return a dictionary that has that topic as a key and a list of all results as the value
	return input_data

def analyze_bing(data): #data is a dictionary of topics (keys) and the corresponding bing search results (values)
	topic_polarity_subjectivity = dict() # dictionary to be returned, contains topic (the key) and polarity, subject as tuple (the value)
	for topic in data: # each topic from twitter
		print topic
		polarity = 0 #the polarity/ sentiment of the statement
		subjectivity = 0 #how subjective the statement is
		number = 0 #counter for number of titles run through
		value = data[topic]
		for bing_search in value:
			polar, subject = sentiment(content)
			polarity += polar
			subjectivity += subject
			number += 1
		topic_polarity_subjectivity[topic] = (polarity/number, subjectivity/number)
	return topic_polarity_subjectivity

# these give the actual results!
topics = trending_topics()
to_be_analyzed = search_bing(topics)
print analyze_bing(to_be_analyzed)