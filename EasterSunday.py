#  File: EasterSunday.py

#  Description: Code to find the easter sunday given a year

#  Student Name: Hussain Bharmal

#  Student UT EID: hab889

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 09/17/2017

#  Date Last Modified: 09/18/2017

def easter_sunday():
	
	y = int(input("Enter year: ")) #input 1
	a = y % 19 #remainder 2
	b = y // 100 #quotient 3
	c = y % 100 #remainder 3
	d = b // 4 #quotient 4
	e = b % 4 #remainder 4
	g = ((8 * b) + 13) // 25 #quotient 5
	h = ((19 * a) + b - d - g + 15) % 30 #remainder 6
	j = c // 4 #quotient 7
	k = c % 4 #remainder 7
	m = (a + (11 * h)) // 319 #quotient 8
	r = ((2 * e) + (2 * j) - k - h + m + 32) % 7 #remainder 9
	n = (h - m + r + 90) // 25 #quotient 10 also month
	p = (h - m + r + n + 19) % 32 #remainder 11 also day

	if n == 1:
		month = "January"
	if n == 2:
		month = "February"
	if n == 3:
		month = "March"
	if n == 4:
		month = "April"
	if n == 5:
		month = "May"
	if n == 6:
		month = "June"
	if n == 7:
		month = "July"
	if n == 8:
		month = "August"
	if n == 9:
		month = "September"
	if n == 10:
		month = "October"
	if n == 11:
		month = "November"
	if n == 12:
		month = "December"


	print("In %s Easter Sunday is on %s %s" % (y,p,month) )

easter_sunday()

