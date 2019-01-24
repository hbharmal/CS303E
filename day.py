def day_of_the_week():
	year = int(input("Enter year: "))
	month = int(input("Enter month: "))
	day = int(input("Enter day: "))

	#commands to show if the date is valid for this algorithm
	while year not in range(1900,2101):
		year = int(input("Enter year: "))

	while month not in range(1,13):
		month = int(input("Enter month: "))

	if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month ==12:
		while day not in range(1,32):
			day = int(input("Enter day: "))
	if month == 4 or month == 6 or month == 9 or month == 11:
		while day not in range(1,31):
			day = int(input("Enter day: "))
	
	#code to find a leap year
	if (year % 4) == 0:
  		if (year % 100) == 0:
       		if (year % 400) == 0:
           		nano = 1
       		else:
           		nano = 0
   		else:
       		nano = 1
	else:
   		nano = 0

   if month == 2:
		if nano = 1:
			while day not in range(1,30):
				day = int(input("Enter day: "))
		elif nano = 0:
			while day not in range(1,29):
				day = int(input("Enter day: "))

	a = month

	#code for rearranging month
	if a in range(3,13):
		a = a - 2
	elif a == 1:
		a = 11
		year =- 1
	elif a == 2:
		a = 12
		year =- 1 

	b = day
	c = (year % 100)
	d = (year // 100)

	#computing the algorithm 
	w = ((13 * a) - 1 ) // 5 
	x = c // 4 
	y = d // 4 
	z = w + x + y + b + c - (2 * d)
	r = z % 7 
	r = (r + 7) % 7

	#computing the day of the week from numbers
	if r == 0:
		day1 = "Sunday"
	if r == 1:
		day1 = "Monday"
	if r == 2:
		day1 = "Tuesday"
	if r == 3:
		day1 = "Wednesday"
	if r == 4:
		day1 = "Thursday"
	if r == 5:
		day1 = "Friday"
	if r == 6:
		day1 = "Saturday"

	#finally printing the result
	print("The day is ", day1)

day_of_the_week()