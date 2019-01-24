#  File: GuessingGame.py

#  Description: Finding out a user's guess in less than 7 tries

#  Student Name: Hussain Bharmal

#  Student UT EID: hab889

#  Course Name: CS 303E

#  Unique Number: 

#  Date Created: 11/14/2017

#  Date Last Modified: 11/14/2017

import sys 

def GuessingGame():

	low = 1
	high = 100

	print("Guessing Game\n\nThink of a number between 1 and 100 inclusive.\nAnd I will guess what it is in 7 tries or less")

	ques = str(input("Are you ready? (y/n): "))

	if ques == "n":
		print("Bye")
		sys.exit()

	max_guesses = 1
	low = 1
	high = 100

	while max_guesses < 8:

		number = (low + high) // 2

		print("Guess %s : The number you thought was %s" %(max_guesses,number))
		guess = int(input(("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")))

		if guess == 1:
			high = number -1
		elif guess == -1:
			low = number + 1
		elif guess == 0:
			print("Thank you for playing the Guessing Game")
			sys.exit()

		max_guesses += 1

	print("Either you guessed a number out of range or had an incorrect entry.")




GuessingGame()