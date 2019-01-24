def main():

	file = open("dna.txt",'r')
	a = int(file.readline()) #number of sequences to compare
	R = [] #array with the sequences inside

	for i in range(0,a*2):
		l = file.readline()
		l = l.rstrip("\n")
		R.append(l)

	file.close()

	#writing a function that finds the longest common substring between two strings: string1 and string2
	def LSF(string1,string2):
		string1 = string1.upper()
		string2 = string2.upper()
		substring = ""
		for i in range(len(string1)):
			match = ""
			for j in range(len(string2)):
				if (i + j) < len(string1) and string1[i+j] == string2[j]:
					match += string2[j]
				elif len(match) > len(substring):
					substring = match
				else:
					match = ""

		if len(substring) == 0 or len(substring) == 1:
			return("No Common Sequence Found")
		else:
			return(substring)
  
	D = []
	for i in range(0,len(R),2):
		substring = LSF(R[i],R[i+1])
		D.append(substring)

	for i in range(1,len(D)+1):
		print("Pair%s: %s" %(i,D[i-1]))

main()
