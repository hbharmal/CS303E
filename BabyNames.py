#  File: BabyNames.py 

#  Description: Baby names dictionary assignment

#  Student Name: Hussain Bharmal	

#  Student UT EID: hab889

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 03/23/2018

#  Date Last Modified: 03/23/2018

import operator
import urllib.request

# returns true if name exists in dictionary
def hasKey(name, dictionary):
	return name in dictionary

# returns all the rankings for a given name
def getRankings(name, dictionary):
	return dictionary.get(name)

# returns all the names that have a rank in all the decades
def getRankInAll(dictionary):
	list = []
	for key in dictionary:
		if 0 not in dictionary[key]:
			list.append(key)
	list.sort()
	return list

# returns all the names that have a rank in a given decade
def getRankInGiven(decade, dictionary):
	names = {}
	index = (decade % 1900) // 10
	for key in dictionary:
		if (dictionary.get(key)[index] != 0):
			names[key] = dictionary[key][index]
	sorted_names = sorted(names.items(), key = lambda x: x[1])
	return sorted_names

# returns all the names that are getting more popular
def getMorePopular(dictionary):
	list = []
	for key in dictionary:
		rankings = dictionary.get(key)
		smaller = True
		if 0 in rankings:
			continue
		for i in range(1, len(rankings)):
			if (rankings[i] >= rankings[i - 1]):
				smaller = False;
				break
		if (smaller):
			list.append(key)
	list.sort()
	return list
		
# returns all the names that are getting less popular
def getLessPopular(dictionary):
	list = []
	for key in dictionary:
		rankings = dictionary.get(key)
		bigger = True
		if 0 in rankings[:len(rankings) - 1]:
			continue;
		stop = (len(rankings) - 1) if (rankings[10] == 0) else len(rankings)
		for i in range(1, stop):
			if (rankings[i] <= rankings[i - 1]):
				bigger = False;
				break
		if (bigger):
			list.append(key)
	list.sort()
	return list

def getHighestRankDecade(name, dictionary):
	rankings = dictionary.get(name)
	index = 0
	for i in range(len(rankings)):
		if (rankings[index] > rankings[i]):
			index = i;
	decade = 1900 + (index * 10)
	return decade			

def main():

	# create an empty dictionary 
	baby_names = {}

	# open the file from the internet
	try:
		data = urllib.request.urlopen("http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt")
	except:
		print("Unable to read file from the internet.")
	

	# read the data
	for line in data:
		line = str (line, encoding = 'utf8')
		text = line.strip().split(' ')
		name = text[0]
		rankings = []
		for i in range(1, len(text)):
			rankings.append(int(text[i]))
		baby_names[name] = rankings

	# close the file
	data.close()

	# interactive program loop 
	while True:
		# print options
		print("Options: ")
		print("Enter 1 to search for names.")
		print("Enter 2 to display data for one name.")
		print("Enter 3 to display all names that appear in only one decade.")
		print("Enter 4 to display all names that appear in all decades.")
		print("Enter 5 to display all names that are more popular in every decade.")
		print("Enter 6 to display all names that are less popular in every decade.")
		print("Enter 7 to quit. \n")

		option = int(input("Enter choice: "))

		if (option == 1):
			name = input("Enter a name: ")
			print()
			if hasKey(name, baby_names):
				print("The matches with their highest ranking decade are: ")
				print("%s %s" %(name, getHighestRankDecade(name, baby_names)))
			else:
				print("%s does not appear in any decade." %(name))
			print()

		elif (option == 2):
			name = input("Enter a name: ")
			print()			
			if hasKey(name, baby_names):
				rankings = baby_names.get(name)
				# print rankings horizontally
				print("%s: " %(name), end = "")
				for i in range(len(rankings)):
					print(rankings[i], end = " ")
				print()
				# print rankings vertically
				for i in range(len(rankings)):
					year = 1900 + (i * 10)
					print("%s: %s" %(year, rankings[i]))
			else:
				print("%s does not appear in any decade." %(name))
			print()

		elif (option == 3):
			decade = int(input("Enter decade: "))
			print("The names are in order of rank: ")
			names_tuple = getRankInGiven(decade, baby_names)
			for name in names_tuple:
				name = list(name)
				print("%s: %s" %(name[0], name[1]))
			print()

		elif (option == 4):
			names_list = getRankInAll(baby_names)
			print("%s names appear in every decade. The names are: " %(len(names_list)))
			for name in names_list:
				print("%s" %(name))
			print()

		elif (option == 5):
			names_list = getMorePopular(baby_names)
			print("%s names are more popular in every decade." %(len(names_list)))
			for name in names_list:
				print("%s" %(name))
			print()

		elif (option == 6):
			names_list = getLessPopular(baby_names)
			print("%s names are less popular in every decade." %(len(names_list)))
			for name in names_list:
				print("%s" %(name))
			print()

		else:
			print("\nGoodbye.")
			break

main()



 












