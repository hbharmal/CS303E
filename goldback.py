#creating a function that lists all the prime numbers from 2 to n
def is_prime (n):
	if (n == 1):
		return False
	limit = int (n ** 0.5) + 1
	div = 2
	while (div < limit):
		if (n % div == 0):
			return False
		div += 1
	return True

def goldback():
	a = int(input("Enter the lower limit: "))
	b = int(input("Enter the upper limit: "))
	
	#three constraints 
	alpha = (a < 4)
	beta = (a % 2 != 0) and (b % 2 != 0)
	gamma = (a>b)

	while alpha or beta or gamma:
		a = int(input("Enter the lower limit: "))
		b = int(input("Enter the upper limit: "))

	P = []
	for num in range(1,b):
		if is_prime(num):
		  P.append(num)

	A = P
	B = []

	for i in range(a,b+1,2):
		B.append(i)

	for i in range(0,len(B)):
		for j in range(0,len(B)):
			if A[i] + A[j] == B[i]:
				print("%s = %s + %s" %(B[i],A[i],A[j]))

goldback()
