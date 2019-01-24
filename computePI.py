'''there are two parts of the function: 
	1) Simulating the throw of a dart for x amount of times
	2) Calculating the accuracy of the value compared to pi
'''

#importing the necessary modules
import random
import math

#part 1 
def computePI(numThrows):
	insideCircle = 0
	for i in range(0,numThrows):
		xPos = random.uniform(-1.0,1.0)
		yPos = random.uniform(-1.0,1.0)
		if math.hypot(xPos,yPos) <= 1:
			insideCircle += 1
	return (insideCircle/numThrows)*4

#part 2
def main():

	def difference(num):
		difference = computePI(num) - math.pi
		a = round(difference,6)
		return a

	values = [100,1000,10000,100000,1000000,10000000]

	for i in range(0,len(values)):
		print("num = ", '{0: <11}'.format(str(values[i])), "Calculated PI = ", format(computePI(values[i]),'.6f'), "Difference = ", format(difference(values[i]),'+.6f'))


main()




