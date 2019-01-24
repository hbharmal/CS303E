# File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Student Name: Hussain Bharmal 

#  Student UT EID: hab889

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 04/08/2018

#  Date Last Modified: 04/08/2018

class Link (object):
	def __init__ (self, col = 0, data = 0, next = None):
		self.col = col
		self.data = data
		self.next = next

	# return a String representation of a Link (col, data)
	def __str__ (self):
		s = "(" + str(self.col) + ", " + str(self.data) + ")"
		return s

class LinkedList (object):
	def __init__ (self):
		self.first = None
		self.num_links = 0

	def insert_link (self, col, data):
		new_link = Link (col, data)
		current = self.first

		if (current == None):
			self.first = new_link
			return

		while (current.next != None):
			current = current.next

		current.next = new_link
		self.num_links += 1

	def delete_link(self, col, data):
		current = self.first
		previous = self.first

		if (current == None):
			return None

		while (current.next != None):
			if (current.data == data and current.col == col):
				previous.next = current.next
				self.num_links -= 1
				return current
			previous = current
			current = current.next

		return None

	# return a String representation of a LinkedList
	def __str__ (self):
		s = ''
		current = self.first
		while (current.next != None):
			s += str(current) + ", "
			current = current.next
		return s

class Matrix (object):
	def __init__ (self, row = 0, col = 0):
		self.row = row
		self.col = col
		self.matrix = []

	# perform assignment operation: matrix[row][col] = data
	def set_element (self, row, col, data):
		linked_list = self.matrix[row]
		current = linked_list.first
		previous = linked_list.first
		
		while (current != None):
			if (current.col == col and data == 0):
				if (current.next == None):
					previous.next == None
				if (previous == current):
					self.matrix[row].first = current.next
				previous.next = current.next 
				break 
			elif (current.col == col and data != 0):
				current.data = data
				break
			elif (current.col > col):
				newLink = Link(col, data)
				previous.next = newLink
				newLink.next = current
				break
			else:
				previous = current
				current = current.next 

	# add two sparse matrices
	def __add__ (self, other):
		if (self.row != other.row or self.col != other.col):
			return None 

		mat = Matrix(self.row, other.col)

		for i in range(self.row):
			new_row = LinkedList()
			list_self = self.get_row(i)
			list_other = other.get_row(i)
			for j in range(self.col):
				sum_add = list_self[j] + list_other[j]
				if (sum_add != 0):
					new_row.insert_link(j, sum_add)
			mat.matrix.append(new_row)

		return mat 

	# multiply two sparse matrices
	def __mul__ (self, other):
		if (self.col != other.row):
			return None

		mat = Matrix(self.row, other.col)

		for i in range(self.row):
			new_row = LinkedList()
			list_self = self.get_row(i)
			for j in range(other.col):
				list_other = other.get_col(j)
				sum_mult = 0
				for k in range(len(list_self)):
					sum_mult += (list_self[k] * list_other[k])
				if (sum_mult != 0):
					new_row.insert_link(i, sum_mult)
			mat.matrix.append(new_row)

		return mat

	# return a list representing a row
	def get_row (self, n):
		linked_list = self.matrix[n]
		final_list = [0 for i in range(self.col)]
		current = linked_list.first
		if (current == None):
			return final_list
		while (current != None):
			final_list[current.col] = current.data
			current = current.next	
		return final_list

	# return a list representing a column
	def get_col (self, n):
		final_list = []
		for i in range(self.row):
			temp_list = self.get_row(i)
			final_list.append(temp_list[n])
		return final_list

	# return a String representation of a matrix
	def __str__ (self):
		s = ''
		for i in range(self.row):
			temp_list = self.get_row(i)
			for j in range(len(temp_list)):
				number = str(temp_list[j])
				number = '{:>4}'.format(number)
				s += number 
			s += "\n"
		return s

def read_matrix (in_file):
	line = in_file.readline().rstrip("\n").split()
	row = int (line[0])
	col = int (line[1])
	mat = Matrix (row, col)

	for i in range (row):
		line = in_file.readline().rstrip("\n").split()
		new_row = LinkedList()
		for j in range (col):
			elt = int (line[j])
			if (elt != 0):
				new_row.insert_link(j, elt)
		mat.matrix.append (new_row)
	line = in_file.readline()

	return mat

def main():
	in_file = open ("./matrix.txt", "r")

	print ("Test Matrix Addition")
	matA = read_matrix (in_file)
	print (matA)
	matB = read_matrix (in_file)
	print (matB)

	matC = matA + matB
	print (matC)

	print ("\nTest Matrix Multiplication")
	matP = read_matrix (in_file)
	print (matP)
	matQ = read_matrix (in_file)
	print (matQ)

	matR = matP * matQ
	print (matR)

	print ("\nTest Setting a Zero Element to a Non-Zero Value")
	matA.set_element (1, 1, 5)
	print (matA)

	print ("\nTest Setting a Non-Zero Elements to a Zero Value")
	matB.set_element (1, 1, 0)
	print (matB)

	print ("\nTest Getting a Row")
	row = matP.get_row(1)
	print (row)

	print ("\nTest Getting a Column")
	col = matQ.get_col(0)
	print (col)
	
	in_file.close()

main()