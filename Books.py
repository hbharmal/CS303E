#  File: Books.py

#  Description: End of semester project

#  Student Name: Hussain Bharmal  

#  Student UT EID: hab889

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 12/05/2017

#  Date Last Modified: 12/05/2017

def parseString(st):
	shouldIContinue = False
	s = ""
	for i in range(0,len(st)):
		if shouldIContinue:
			shouldIContinue = False
			continue
		if st[i] == "'":
			if st[i:i+2] == "'s":
				shouldIContinue = True
			elif st[i+1].isalpha():
				s += st[i]
		elif st[i].isalpha() or st[i].isspace():
			s += st[i]
		else:
			s += " "
	return s 

def createWordDict():
	word_dict = {}
	wordsFile = open("words.txt","r")
	for line in wordsFile:
		line = line.strip()
		word_dict[line] = 1 
	return word_dict

def getWordFreq(file):
	in_file = open(file,"r")
	content = []
	word_freq = {}
	for line in in_file:
		line = line.strip()
		line = parseString(line)
		line = line.split()
		for word in line:
			if word not in content:
				content.append(word)
				word_freq[word] = 1
			else:
				word_freq[word] += 1
	in_file.close()

	capital_words = []
	word_dict = createWordDict()

	for key in word_freq:
		if key[0].isupper():
			capital_words.append(key)

	for word in capital_words:
		if word.lower() in word_freq:
			word_freq[word.lower()] += word_freq[word]
		elif word.lower() in word_dict:
			word_freq[word.lower()] = 1

	for word in capital_words:
		del word_freq[word]

	return word_freq

def wordComparion(author1, wordFreq1, author2, wordFreq2):
	#Author 1 
	dist_words_1 = len(wordFreq1.values())
	total_words_1 = 0
	for key in wordFreq1:
		total_words_1 += wordFreq1[key]
	ratio_1 = 100 * float(dist_words_1 / total_words_1)

	#Author 2 
	dist_words_2 = len(wordFreq2.values())
	total_words_2 = 0
	for key in wordFreq2:
		total_words_2 += wordFreq2[key]
	ratio_2 = 100 * float(dist_words_2 / total_words_2)

	#Comparing 
	A1 = set(wordFreq1.keys())
	A2 = set(wordFreq2.keys())

	author1_unique = A1 - A2
	author2_unique = A2 - A1

	a = len(author1_unique)
	b = len(author2_unique)
	
	#iterating over set to find total word frequency
	a2 = 0 
	for word in author1_unique:
	  a2 += wordFreq1[word] 
	
	b2 = 0
	for word in author2_unique:
	  b2 += wordFreq2[word] 
	
	ratio_1_distinct = 100 * float(a2 / total_words_1)
	ratio_2_distinct = 100 * float(b2 / total_words_2)


	print("%s" %(author1))
	print("Total distinct words = %d" %(dist_words_1))
	print("Total words (including duplicates) = %d" %(total_words_1))
	print("Ratio of total distinct words to total words) = %f" %(ratio_1))
	print()
	print("%s" %(author2))
	print("Total distinct words = %d" %(dist_words_2))
	print("Total words (including duplicates) = %d" %(total_words_2))
	print("Ratio of total distinct words to total words) = %f" %(ratio_2))
	print()
	print("%s used %d words that %s did not use." %(author1, a, author2))
	print("Relative frequency of words used by %s not in common with %s = %f" %(author1, author2, ratio_1_distinct))
	print()
	print("%s used %d words that %s did not use." %(author2, b, author1))
	print("Relative frequency of words used by %s not in common with %s = %f" %(author2, author1, ratio_2_distinct))


def main():

	book1 = input("Enter name of first book: ")
	book2 = input("Enter name of second book: ")
	print()

	author1 = input("Enter last name of first author: ")
	author2 = input("Enter last name of second author: ")
	print()

	wordFreq1 = getWordFreq(book1)
	wordFreq2 = getWordFreq(book2)

	wordComparion(author1, wordFreq1, author2, wordFreq2)

main()
	






