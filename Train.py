#  File: Train.py

#  Description: Drawing a train using Turtle graphics

#  Student Name: Hussain Bharmal

#  EID: hab889

#  Date Created: 02/12/2018

#  Date Last Modified: 02/13/2018

import turtle, math

def drawRail(turtle, length, width, x, y):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.goto(x, y - width)
	turtle.goto(x + length, y - width)
	turtle.goto(x + length, y)
	turtle.penup()
	return(drawStuds(turtle, x, y))

def drawStuds(turtle, x, y):
	if (x > 250):
		return
	else:
		return(drawRail(turtle, 20, 5, x + 40, y))

def drawBoltsVert(turtle, x, y, size):
	if (x > 310):
		return
	else:
		return(drawCircleBoltsVert(turtle, x, y, size))

def drawCircleBoltsVert(turtle, x, y, size):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(size)
	turtle.end_fill()
	turtle.penup()
	return (drawBoltsVert(turtle, x + 10, y, size))


def drawBoltsHor(turtle, x, y, size):
	if (y > 102):
		return
	else:
		return(drawCircleBoltsHor(turtle, x, y, size))

def drawCircleBoltsHor(turtle, x, y, size):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(size)
	turtle.end_fill()
	turtle.penup()
	return (drawBoltsHor(turtle, x, y + 10, size))

def drawLine(turtle, x, y, x2, y2):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.goto(x2, y2)
	turtle.penup()

def drawCircle(turtle, x, y, dim):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.circle(dim)
	turtle.penup()

def drawShape(turtle, x, y, dim, stp):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.circle(dim, steps = stp)
	turtle.penup()

def arc(turtle, x, y, size, degrees):
	turtle.goto(x, y)
	turtle.pendown()
	for iter in range (degrees):
		turtle.forward(size)
		turtle.right(1)
	turtle.penup()

def drawRectangle(turtle, x, y, length, width):
	drawLine(turtle, x, y, x + length, y)
	drawLine(turtle, x + length, y, x + length, y + width)
	drawLine(turtle, x + length, y + width, x, y + width)
	drawLine(turtle, x, y + width, x, y)

def drawSpoke(turtle, x, y, spokeSize):
	degrees = 360
	turtle.goto(x, y)
	turtle.pendown()
	if spokeSize == .25:
		for iter in range (degrees):
			if (iter % 45 == 0):
				turtle.left(100)
				turtle.forward(30)
				turtle.backward(30)
				turtle.right(100)
				turtle.left(80)
				turtle.forward(30)
				turtle.backward(30)
				turtle.right(80)
			turtle.forward(spokeSize)
			turtle.right(1)
	elif spokeSize == .15:
		for iter in range (degrees):
			if (iter % 45 == 0):
				turtle.left(100)
				turtle.forward(26.5)
				turtle.backward(26.5)
				turtle.right(100)
				turtle.left(80)
				turtle.forward(26.5)
				turtle.backward(26.5)
				turtle.right(80)
			turtle.forward(spokeSize)
			turtle.right(1)
	turtle.penup()

def drawWheels(turtle, x, y, radius, spokeSize):
	drawCircle(turtle, x, y, radius)
	drawCircle(turtle, x, y + 10, radius - 10)
	if radius == 55:
		drawSpoke(turtle, x, y + (radius + 15), spokeSize)
	elif radius == 45:
		drawSpoke(turtle, x, y + (radius + 7.5), spokeSize)

def main():
  
  turtle.title ('Train')
  turtle.setup (800, 800, 0, 0)
  turtle1 = turtle.Turtle()
  turtle1.pensize(2)
  turtle.tracer(100000)

  # draw rail
  drawLine(turtle1, -350, -200, 350, -200)
  drawLine(turtle1, -350, -220, 350, -220)
  drawStuds(turtle1, -350, -220)

  turtle2 = turtle.Turtle()
  turtle2.pensize(2)

  # draw wheels
  turtle2.color('red')
  drawWheels(turtle2, -200, -200, 55, .25)
  drawWheels(turtle2, 20.74, -200, 45, .15)
  drawWheels(turtle2, 214.26, -200, 45, .15)

  turtle2.color('blue')

  # draw back of train body
  drawLine(turtle2, -300, 150, -300, -150)
  drawLine(turtle2, -300, -150, -272.5, -150)
  turtle2.left(90)
  arc(turtle2, -272.5, -150, 1.25, 180)
  turtle2.left(90)
  turtle2.pendown()
  turtle2.forward(27.5)
  turtle2.left(90)
  turtle2.forward(300)
  turtle2.left(90)
  turtle2.forward(197)
  drawRectangle(turtle2, -330, 151, 260, 40)

  # draw main train body
  drawLine(turtle2, -101.76, 110, 312.20, 110)
  drawRectangle(turtle2, 30, 110, 70, 25)
  drawRectangle(turtle2, 50, 135, 30, 12)

  # draw smokestack 
  drawLine(turtle2, 190, 110, 160, 196.6)
  turtle2.goto(160, 196.6)
  turtle2.pendown()
  turtle2.right(180)
  turtle2.forward(100)
  turtle2.left(120)
  turtle2.forward(30)
  turtle2.left(60)
  turtle2.forward(70)
  turtle2.left(60)
  turtle2.forward(30)
  turtle2.penup()
  turtle2.right(60)
  drawLine(turtle2, 230, 110, 260, 196.6)

  # bottom train body
  turtle2.goto(-101.76, -149)
  turtle2.penup()
  turtle2.right(180)
  turtle2.pendown()
  turtle2.forward(50)
  turtle2.left(90)
  arc(turtle2, -51.76, -148.75, 1.25, 180)
  turtle2.pendown()
  turtle2.left(90)
  turtle2.forward(50)
  turtle2.left(90)
  arc(turtle2, 141.76, -148.46, 1.25, 180)
  turtle2.left(90)
  turtle2.pendown()
  turtle2.forward(27.5)
  turtle2.penup()
  drawLine(turtle2, 312.20, -147.21, 312.20, 110)

  # draw steel bolt tracks
  drawRectangle(turtle2, -102, -5, 414, 15)
  drawBoltsVert(turtle2, -96, 0, 2)

  drawRectangle(turtle2, -10, 10, 15, 100)
  drawBoltsHor(turtle2, -3, 16, 2)
  drawRectangle(turtle2, 207, 10, 15, 100)
  drawBoltsHor(turtle2, 214, 16, 2)

  # draw polygon in front of train
  turtle2.penup()
  turtle2.goto(312.50, -147.21)
  turtle2.pendown()
  turtle2.forward(60)
  turtle2.left(120)
  turtle2.forward(60)
  turtle2.left(60)
  turtle2.forward(30)

  # draw rectangles in front of train
  drawRectangle(turtle2, 312.20, -70, 20, 150)
  drawRectangle(turtle2, 332.20, -35, 10, 75)

  # draw windows in caboose
  turtle2.color('gray')
  turtle2.begin_fill()
  drawRectangle(turtle2, -280, 40, 70, 80)
  turtle2.end_fill()
  turtle2.begin_fill()
  drawRectangle(turtle2, -190, 40, 70, 80)
  turtle2.end_fill()

  turtle2.color('blue')
  drawRectangle(turtle2, -280, 40, 70, 80)
  drawRectangle(turtle2, -190, 40, 70, 80)


  # hide turtle
  turtle2.hideturtle()

  # finished drawing
  turtle.done()

main()