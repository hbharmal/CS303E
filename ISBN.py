#  File: ISBN.py

#  Description: Check and see if an ISBN is valid or not

#  Student Name: Hussain Bharmal	

#  Student UT EID: hab889

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/29/2017

#  Date Last Modified: 10/30/2017

def main():

	in_file = open("isbn.txt","r")

	ISBNS = []
	line = in_file.readline()
	line = line.rstrip("\n")
	ISBNS.append(line)
	while line != "":
		line = in_file.readline()
		line = line.rstrip("\n")
		ISBNS.append(line)
	del ISBNS[-1]

	#function to clean the ISBN
	def clean(ISBN):
		ISBN = ISBN.strip()
		for i in ISBN:
			if (i != '0') and (i != '1') and (i != '2') and (i != '3') and (i != '4') and (i != '5') and (i != '6') and (i != '7') and (i != '8') and (i != '9') and (i != 'x') and (i != 'X'):
				ISBN = ISBN.replace(i,'')
		newISBN = str(ISBN)
		return newISBN

	#function to get partial sum with a string as an input
	def partial_sum(number):
		sum1 = 0
		par_sums = []
		for i in range(0,len(number)):
			if (number[i] == 'x') or (number[i] == 'X'):
				sum1 += 10
				par_sums.append(sum1)
			else:
				sum1 += int(number[i])
				par_sums.append(sum1)
		return par_sums

	#function to get partial sum with an input of a list of numbers
	def partial(array):
		sum1 = 0
		par_sums = []
		for i in range(0,len(array)):
			sum1 += array[i]
			par_sums.append(sum1)
		return par_sums

	#function to see if the ISBN is valid
	def isReal(ISBN):
		real = ['0','1','2','3','4','5','6','7','8','9','x','X','-']
		for i in range(0,len(ISBN)):
			if ISBN[i] not in real:
				return False
			elif (ISBN[i] == 'X' or ISBN[i] == 'x') and (i < 10):
				return False
		a = clean(ISBN)
		b = partial_sum(a)
		c = partial(b)
		if len(clean(a)) > 10:
			return False
		elif (c[len(c) - 1] % 11) != 0:
			return False
		else:
			return True 

	#opening file to write on
	out_file = open("isbnOut.txt",'w')

	#block of code to write on the output file
	for i in range(0,len(ISBNS)):
		if isReal(ISBNS[i]) == True:
			out_file.write("%s valid" %(ISBNS[i]) + '\n')
		else:
			out_file.write("%s invalid" %(ISBNS[i]) + '\n')

	out_file.close()
	in_file.close()

main()









