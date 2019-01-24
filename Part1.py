def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def bunnyEars(bunnies):
	if bunnies == 0:
		return 0
	else:
		return bunnies + bunnyEars(bunnies-1)

def fibanacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else: 
		return fibanacci(n-1) + fibanacci(n-2)

def bunnyEars2(bunnies):
	if bunnies == 1:
		return 2
	elif bunnies == 2:
		return 3
	else:
		return bunnies + bunnyEars2(bunnies-1)

def triangle(rows):
	if rows == 1:
		return 1
	else:
		return rows + triangle(rows-1)

def sumDigits(n):
	if n % 10 == 0:
		return n
	else:
		return (m+1)

def count7(n):
	if n == 0:
		return 0
	elif (n % 10) == 7:
		return 1 + count7(n//10)
	else:
		return count7(n//10)

def count8(n):
	if n == 0:
		return 0
	elif (n % 10) == 8 and ((n//10) % 10) == 8:
		return 2 + count8(n//10)
	elif (n % 10) == 8:
		return 1 + count8(n//10)
	else:
		return count8(n//10)

def powerN(base,n):
	None 

def countX(str):
	if len(str) == 0:
		return 0
	else:
		if str[0] == "x":
			return 1 + countX(str[1:])
		else:
			return countX(str[1:])

def countHi(str):
	if len(str) == 0:
		return 0
	else:
		if str[0:1]






			