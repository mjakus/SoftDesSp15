# search twitter for trending topics, calculate average subjectivity and sentiment about each thing?

from pattern.web import Bing, SEARCH, plaintext
from pattern.en import sentiment
from pattern.search import search
from pattern.web import Twitter

def trending_topics():
	topics = Twitter().trends(cached=False)
	return topics


engine = Bing(license = None)
def search_bing(input): # takes in a list of topics to search
	input_data = dict()
	vals_for_dict = []
	for topic in input: # for each trending topic
		for i in range(1,10): # do this 10 times
			for result in engine.search(topic, type = SEARCH, start = i): # for each result for that topic
				vals_for_dict.append([repr(plaintext(result.text))]) # append the results to a list of the results for that topic
		input_data[topic] = vals_for_dict # return a dictionary that has that topic as a key and a list of all results as the value
	return input_data

def analyze_bing(data): #data is a dictionary
	topic_polarity_subjectivity = dict() # dictionary to be returned, contains topic (the key) and polarity, subject as tuple (the value)
	for topic in data: # each topic from twitter
		polarity = 0 #the polarity/ sentiment of the statement
		subjectivity = 0 #how subjective the statement is
		number = 0 #counter for number of titles run through
		value = data[topic]
		for bing_search in value:
			polar, subject = sentiment(bing_search)
			print bing_search
			polarity += polar
			subjectivity += subject
			number += 1
		topic_polarity_subjectivity[topic] = (polarity/number, subjectivity/number)
	return topic_polarity_subjectivity

# to test sentiment
# test_case = ["I hate you"]
# print sentiment(test_case)

# other things to see!
# print trending_topics()
# print search_bing(topics)


# these give the actual results!
topics = trending_topics()
to_be_analyzed = search_bing(topics)
print analyze_bing(to_be_analyzed)
