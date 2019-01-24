#  File: Grid.py

#  Description: Find the greatest product in a grid

#  Student Name: Hussain Bharmal

#  Student UT EID: hab889

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/31/2017

#  Date Last Modified: 11/01/2017

def main():

	file = open("grid.txt","r")

	#define the grid length "a"
	a = file.readline()
	a = a.strip()
	a = int(a)

	#read each line into a 2D grid called "grid"
	grid = []
	for i in range(0,a):
		b = file.readline()
		b = b.strip()
		b = b.split()
		for j in range(a):
		  b[j] = int(b[j])
		grid.append(b)

	#products of rows
	Prods1 = [] 
	for k in range(a):
		for i in range(a-3):
			prod = 1
			for j in range(i,i+4):
				prod = prod * grid[k][j]
			Prods1.append(prod)

	#products of columns
	Prods2 = []
	for k in range(a):
		for i in range(a-3):
			prod = 1
			for j in range(i,i+4):
				prod = prod * grid[j][k]
			Prods2.append(prod)

	#products of diagonals from L to R
	Prods3 = []
	for i in range(0,a-3):
		for j in range(0,a-3):
			prod = 1
			for k in range(4):
				prod = prod * grid[i+k][j+k]
			Prods3.append(prod)

	#products of diagonals from R to L
	Prods4 = []
	for i in range(0,a-3):
		for j in range(3,a):
			prod = 1
			for k in range(4):
				prod = prod * grid[i+k][j-k]
			Prods4.append(prod)

	#calculate the max of each array
	max1 = max(Prods1)
	max2 = max(Prods2)
	max3 = max(Prods3)
	max4 = max(Prods4)

	#calculate the total maximum
	Maximum = max(max1,max2,max3,max4)

	print("The greatest product is %s" %(Maximum))

main()
