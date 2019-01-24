#  File: Spiral.py

#  Description: Finding the neighbours of a number in a spiral

#  Student Name: Hussain Bharmal, Reethika Thakkalapally

#  Student UT EID: hab889, rt24757

#  Course Name: CS 303E

#  Unique Number: 51345, 51345

#  Date Created: 11/20/2017

#  Date Last Modified: 11/20/2017

import sys

def changeDirection(current):
	if current == [1,0]:
		return [0,1]
	elif current == [0,1]:
		return [-1,0]
	elif current == [-1,0]:
		return [0,-1]
	elif current == [0,-1]:
		return [1,0]

def getNeighbours(array,n):
	ind = [(index, row.index(n)) for index, row in enumerate(array) if n in row]
	i = ind[0][0] 
	j = ind[0][1]
	dim = len(array)
	if (i == 0) or (j == 0) or (i == (dim-1)) or (j == (dim-1)):
		return ("Number on Outer Edge")
	else:
		result = [[0 for i in range(3)] for j in range(3)]
		result[0][0] = array[i-1][j-1]
		result[0][1] = array[i-1][j]
		result[0][2] = array[i-1][j+1]
		result[1][0] = array[i][j-1]
		result[1][1] = array[i][j]
		result[1][2] = array[i][j+1]
		result[2][0] = array[i+1][j-1]
		result[2][1] = array[i+1][j]
		result[2][2] = array[i+1][j+1]
	return result

def main():
	dim = int(input("Enter dimension: "))
	if (dim % 2 == 0):
		dim += 1

	num = int(input("Enter number in spiral: "))
	if num not in range(1,num**2):
		print("Number not in Range")
		sys.exit()

	result = [[0 for i in range(dim)] for j in range(dim)]

	#Stating initial conditions to construct a spiral with arbitrary size 
	amount = 1
	number = 0
	x = (dim-1)//2
	y = (dim-1)//2
	number += 1
	result[x][y] = number
	current = [0,-1]

	#Special condition when encountering the last row/column
	doBreak = False

	for i in range(0,dim):

		current = changeDirection(current)
		for j in range(0,amount):
			number += 1
			x += current[0]
			y += current[1]
			result[y][x] = number

		current = changeDirection(current)
		for j in range(0,amount):
			number += 1
			x += current[0]
			y += current[1]
			result[y][x] = number

		amount += 1

		if amount == dim:
			doBreak = True
			current = changeDirection(current)
			for j in range(0,amount-1):
				number += 1
				x += current[0]
				y += current[1]
				result[y][x] = number

		if doBreak:
			break 

	numNeighbours = getNeighbours(result,num)

	for i in range(0,len(numNeighbours)):
		for j in range(0,len(numNeighbours[i])):
			print(numNeighbours[i][j],end=" ")
		print()

main()












