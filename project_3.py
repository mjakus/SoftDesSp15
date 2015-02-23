# search twitter for trending topics, calculate average subjectivity and sentiment about each thing?

from pattern.web import Bing, SEARCH, plaintext
from pattern.en import *
from pattern.search import search
from pattern.web import Twitter

def trending_topics():
	topics = Twitter().trends(cached=False)
	return topics


engine = Bing(license = None)
def search_bing(input):
	input_data = []
	for i in range(1,10):
		for result in engine.search(input, type = SEARCH, start = i):
			input_data = input_data + [repr(plaintext(result.text))]
	return input_data

def analyze_bing(data):
	polarity = 0 #the polarity/ sentiment of the statement
	subjectivity = 0 #how subjective the statement is
	number = 0 #counter for number of titles run through
	for title in data:
		polar, subject = sentiment(title)
		polarity = polarity + polar
		subjectivity = subjectivity + subject
		number += 1
	return polarity/number, subjectivity/number



print trending_topics()
topics = trending_topics()
Oscar_titles = search_bing('Oscars')
print analyze_bing(Oscar_titles)
