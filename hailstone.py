def hailstone():

	#asks the user to input the starting and ending range of values
	a = int(input("Enter starting number of the range: "))
	b = int(input("Enter ending number of the range: "))

	#checks to see if the algorithm conditions are true 
	while (a < 0) or (b < 0) or (a > b):
		a = int(input("Enter starting number of the range: "))
		b = int(input("Enter ending number of the range: "))
  	
  	#creates an array of numbers from a to b inclusive
	r = []
	for i in range(a,b+1):
	  r.append(i)


	l = []

	#computes the hailstone algorithm 
	for n in range(a,b+1):
		i = 0
		while n > 1:
			if (n % 2) == 0:
				n = n // 2
				i += 1
			else: 
				n = (3 * n) + 1
				i += 1
		l.append(i)
	
	m = max(l)
	c = [i for i, j in enumerate(l) if j==m]
	
	if c != int: #if there are multiple maximum cycle lengths 
	  c1 = max(c)
	  q1 = r[c1]
	else: 
	  for i in c:
	    c1 = i
	  q1 = r[c1]
	
	#finally printing the result
	print("The number %s has the longest cycle length of %s" % (q1,m))
	
hailstone()