#  File: ExpressionTree.py

#  Description: Expression tree assignment

#  Student's Name: Hussain Bharmal

#  Student's UT EID: hab889

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 04/11/2018

#  Date Last Modified: 04/11/2018

class Stack(object):
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def isEmpty(self):
		return (len(self.stack) == 0)

	def size(self):
		return (len(self.stack))

class Node(object):
	def __init__(self, data = None):
		self.left = None
		self.right = None
		self.data = data

class Tree(object):
	def __init__(self):
		self.root = Node()
		self.operators = ['+', '-', '*', '/']
		self.prefix = []
		self.postfix = []

	def createTree(self, expr):
		token_list = expr.strip().split()
		stack = Stack()
		current = self.root

		for token in token_list:
			if (token == "("):
				new_node = Node()
				current.left = new_node
				stack.push(current)
				current = current.left
			elif (token in self.operators):
				new_node = Node()
				current.data = token 
				current.right = new_node
				stack.push(current)
				current = current.right
			elif (token == ")"):
				current = stack.pop() if (not stack.isEmpty()) else current
			else:
				current.data = token
				current = stack.pop()


	def evaluate(self, aNode):
		current = aNode
		if (current.data == "+"):
			return self.evaluate(current.left) + self.evaluate(current.right)
		elif (current.data == "-"):
			return self.evaluate(current.left) - self.evaluate(current.right)
		elif (current.data == "*"):
			return self.evaluate(current.left) * self.evaluate(current.right)
		elif (current.data == "/"):
			return self.evaluate(current.left) / self.evaluate(current.right)
		else:
			return eval(current.data)

	def preOrder(self, aNode):
		current = aNode
		if (current == None):
			return
		print(current.data, end = " ")
		self.preOrder(current.left)
		self.preOrder(current.right)

	def postOrder(self, aNode):
		current = aNode
		if (current == None):
			return
		self.postOrder(current.left)
		self.postOrder(current.right)
		print(current.data, end = " ")

def main():

	# read file
	in_file = open("expression.txt", "r")
	expression = in_file.readline().strip()

	# create instance of expression tree
	expression_tree = Tree()

	# build the tree
	expression_tree.createTree(expression)

	# calculate and print total, preorder, postorder
	print("%s = %s" %(expression, expression_tree.evaluate(expression_tree.root)))
	print("Prefix Expression: ", end = "")
	expression_tree.preOrder(expression_tree.root)
	print()
	print("Postfix Expression: ", end = "")
	expression_tree.postOrder(expression_tree.root)
	print()

	# close the file
	in_file.close()

main()
			
