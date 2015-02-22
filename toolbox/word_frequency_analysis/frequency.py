""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg 

	Maggie Jakus 2/21/15
	"""

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name, 'r')
	
	punct = string.punctuation

	d = dict()

	lines = f.readlines()
	curr_line = 0
	all_words = []

	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line+=1
	lines = lines[curr_line+1:]

	for line in lines:
		words_per_line = string.split(line)
		for word in words_per_line:
			word = word.lower()
			for char in punct:
				word = word.replace(char, "")
			if word not in all_words:
				all_words.append(word)
			if word not in d:
				d[word] = 1
			else:
				d[word] += 1

	return d



def get_top_n_words(words_and_keys, n):
	""" Takes a dictionary of words and their occurrences as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		words_and_keys: a dictionary of words and their occurrences (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	ordered_by_frequency = sorted(words_and_keys, key = words_and_keys.get, reverse = True)
			
	return ordered_by_frequency[:n]


dictionary = get_word_list('book.txt')
print get_top_n_words(dictionary, 4)

