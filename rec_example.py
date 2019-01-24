#  File: Art.py

#  Description: Art using recursion

#  Student Name: Hussain Bharmal

#  Student UT EID: hab889

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 03/02/2018

#  Date Last Modified: 03/02/2018

import turtle
import random
import os

def drawSquare(ttl, n2):
	for k in range (0, 4):
		ttl.pendown()
		ttl.forward(n2)
		ttl.left(90)
		ttl.penup()

def recurShape(shape, ttl, n, n2):
	for i in range (0, n):
		shape(ttl, n2)
		ttl.left(90)
	ttl.penup()
	ttl.forward(100)

def randomPoint():
	x = random.randint(0, 200)
	return x

def main():

	# user defined level of recursion
	iters = int(input("Enter a level of recursion between 1 and 6: "))
	while iters < 1 or iters > 6:
			iters = int(input("Enter a level of recursion between 1 and 6: "))

	# set up screen size and color
	turtle.setup (800, 800, 0, 0)
	turtle.tracer (10000)
	turtle.bgcolor("white")

	# create turtle object
	ttl = turtle.Turtle()

	# set turtle speed
	ttl.speed(10)

	# arrays
	colorList = ["blue", "red", "green"]

	for i in range (0, 3):
		ttl.color(colorList[i])
		recurShape(drawSquare, ttl, iters, 100)
		ttl.goto(randomPoint(), randomPoint())

	pic = ttl.getscreen()

	outName = os.path.basename(__file__)[:-2]+'eps'
	turtScrn = turtle.getscreen()
	turtScrn.getcanvas().postscript(file=outName)
	
main()
