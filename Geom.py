import math

class Point (object):
	# constructor
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
    
	# get distance 
	def dist(self, other):
		return math.hypot(self.x - other.x, self.y - other.y)

	# get a string representation of a Point object
	def __str__ (self):
		return '(' + str(self.x) + ", " + str(self.y) + ")"

	# test for equality
	def __eq__(self, other):
		tol = 1.0e-16
		return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
	# constructor 
	def __init__(self, radius = 1, x = 0, y = 0):
		self.radius = radius
		self.center = Point(x, y)

	# compute circumference 
	def circumference(self):
		return 2.0 * math.pi * self.radius

	# compute area
	def area(self):
		return math.pi * self.radius * self.radius

	# determine if point is strictly inside circle 
	def point_inside(self, p):
		return (self.center.dist(p) < self.radius)

	# determine if a circle is strictly inside this circle
	def circle_inside(self, c):
		distance = self.center.dist(c.center)
		return (distance + c.radius) < self.radius

	# determine if a circle c intersects this circle (non-zero area of overlap)
	def does_intersect(self, c):
		distance = self.center.dist(c.center)
		return (self.radius + c.radius) > distance

	# determine the smallest circle that circumscribes a rectangle
	# the circle goes through all the vertices of the rectangle
	@staticmethod
	def circle_circumscribes(r):
		mid_x = (r.length() / 2) + r.ul.x
		mid_y = (r.width() / 2) + r.lr.y
		radius =  r.ul.dist(r.lr) / 2
		return Circle(radius, mid_x, mid_y)

	# string representation of a circle
	def __str__(self):
		return "Center: %s, Radius: (%.1f)" %(self.center, self.radius)

	# test for equality of radius
	def __eq__(self, other):
		tol = 1.0e-16
		return (abs(self.radius - other.radius) < tol)

class Rectangle (object):
	# constructor 
	def __init__(self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 1):
		if ((ul_x < lr_x) and (ul_y > lr_y)):
			self.ul = Point(ul_x, ul_y)
			self.lr = Point(lr_x, lr_y)
		else:
			self.ul = Point(0, 1)
			self.lr = Point(1, 0)

	# determine length of Rectangle (distance along the x axis)
	def length(self):
		return (abs(self.ul.x - self.lr.x))

	# determine width of Rectangle (distance along the y axis)
	def width(self):
		return (abs(self.ul.y - self.lr.y))

	# determine the perimiter
	def perimeter(self):
		return (2 * abs(self.ul.x - self.lr.x)) + (2 * abs(self.ul.y - self.lr.y)) 

	# determine the area
	def area(self):
		return (abs(self.ul.x - self.lr.x) * abs(self.ul.y - self.lr.y)) 

	# determine if a point is strictly inside the Rectangle
	def point_inside(self, p):
		return (p.x > self.ul.x and p.x < self.lr.x) and (p.y > self.ul.y and p.y < self.lr.y)

	# determine if another Rectangle is strictly inside this Rectangle 
	def rectangle_inside(self, r):
		return (r.ul.x > self.ul.x and r.lr.x < self.lr.x) and (r.ul.y > self.ul.y and r.lr.y < self.lr.y)

	# determine if two Rectangles overlap (non-zero area of overlap) #COMPLETE
	def does_intersect(self, other):
		if (self.ul.x < other.lr.x and self.lr.x > other.ul.x and self.ul.y < other.lr.y and self.lr.y > other.ul.y):
			return False
		return True

	# determine the smallest rectangle that circumscribes a circle
	# sides of the rectangle are tangents to the circle 
	@staticmethod 
	def rect_circumscribe(c):
		ul = Point(c.center.x - c.radius, c.center.y + c.radius)
		lr = Point(c.center.x + c.radius, c.center.y - c.radius)
		return Rectangle(ul.x, ul.y, lr.x, lr.y)

	# give string representation of a rectangle
	def __str__(self):
		return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

	# determine if two rectangles have the same length and width
	def __eq__(self, other):
		tol = 1.0e-16
		return (abs(self.length() - other.length())) < tol and (abs(self.width() - other.width())) < tol

def main():

	# read file
	in_file = open("geom.txt", "r")
	coordinates = []
	for line in in_file:
		line = line.strip().split(" ")
		coordinates.append(line)

	# Create instances of shapes
	pointP = Point(float(coordinates[0][0]), float(coordinates[0][1]))
	pointQ = Point(float(coordinates[1][0]), float(coordinates[1][1]))
	circleC = Circle(float(coordinates[2][2]), float(coordinates[2][0]), float(coordinates[2][1]))
	circleD = Circle(float(coordinates[3][2]), float(coordinates[3][0]), float(coordinates[3][1]))
	rectangleG = Rectangle(float(coordinates[4][0]), float(coordinates[4][1]), float(coordinates[4][2]), float(coordinates[4][3]))
	rectangleH = Rectangle(float(coordinates[5][0]), float(coordinates[5][1]), float(coordinates[5][2]), float(coordinates[5][3]))

	# Print in proper format
	print("Coordinates of P: %s" %(pointP))
	print("Coordinates of Q: %s" %(pointQ))
	print("Distance between P and Q: %.4f" %(pointP.dist(pointQ)))
	print("Circle C: %s" %(circleC))
	print("Circle D: %s" %(circleD))
	print("Circumference of C: %.4f" %(circleC.circumference()))
	print("Area of D: %.4f" %(circleD.area()))
	print("P %s inside C" %("is" if circleC.point_inside(pointP) else "is not"))
	print("C %s inside D" %("is" if circleD.circle_inside(circleC) else "is not"))
	print("C %s intersect D" %("does" if circleC.does_intersect(circleD) else "does not"))
	print("C %s equal to D" %("is" if (circleC == circleD) else "is not"))
	print("Rectangle G: %s" %(rectangleG))
	print("Rectangle H: %s" %(rectangleH))
	print("Length of G: %.1f" %(rectangleG.length()))
	print("Width of H: %.1f" %(rectangleH.width()))
	print("Perimeter of G: %.1f" %(rectangleG.perimeter()))
	print("Area of H: %.1f" %(rectangleH.area()))
	print("P %s inside G" %("is" if rectangleG.point_inside(pointP) else "is not"))
	print("G %s inside H" %("is" if rectangleH.rectangle_inside(rectangleG) else "is not"))
	print("G %s overlap H" %("does" if rectangleH.does_intersect(rectangleG) else "does not"))
	print("Circle that circumscribes G: %s" %(Circle.circle_circumscribes(rectangleG)))
	print("Rectangle that circumscribes D: %s" %(Rectangle.rect_circumscribe(circleD)))
	print("Rectangle G %s equal to H" %("is" if (rectangleG == rectangleH) else "is not"))
	
	# close the file
	in_file.close()

main()
