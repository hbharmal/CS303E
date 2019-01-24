# File: Deal.py

# Description: To prove Marilyn vos Savant was right about the deal game

# Student Name: Hussain Bharmal

# Student UT EID: hab889

# Course Name: CS 303E

# Unique Number: 51345

# Date Created: 10/17/2017

# Date Last Modified: 10/17/2017

import random

#functiom to return the other value 
def other(a,b):
	for i in range(1,4):
		if a != i and b != i:
			c = i
	return c

def main():

	num_plays = int(input("Enter the number of times you want to play this game: "))

	print("  Prize      Guess       View    New Guess ")

	wins = 0
	plays = 0
  
	while num_plays > plays:
		
		plays += 1

		prize = random.randint(1,3)
		print("   ",prize,end="          ")

		guess = random.randint(1,3)
		print(guess,end="          ")

		view = other(prize,guess)
		print(view,end="          ")

		newGuess = other(guess,view)
		print(newGuess)

		if prize == newGuess:
			wins += 1
	
	prob_switching = round((wins/num_plays),2)
	prob_not = round((1 - prob_switching),2)

	print("Probability of winning if you switch: ", prob_switching)
	print("Probability of winning if you do not switch ", prob_not)

main()




