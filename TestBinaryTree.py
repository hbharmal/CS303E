#  File: TestBinaryTree.py

#  Description: Binary Tree assignment

#  Student Name: Hussain Bharmal

#  Student UT EID: hab889

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 04/15/2018

#  Date Last Modified: 04/15/2018

import random

class Node (object):
	def __init__ (self, data):
		self.data = data
		self.left = None 
		self.right = None 


class Tree (object):
	def __init__(self):
		self.root = None 

	# returns true if two binary trees are similar
	def is_similar (self, other):
		pNode_self = self.root
		pNode_other = other.root
		return self.is_similar_helper(pNode_self, pNode_other)

	def is_similar_helper (self, pNode_self, pNode_other):
		if (pNode_self == None and pNode_other == None):
			return True 
		elif ((pNode_self == None and pNode_other != None) or (pNode_self != None and pNode_other == None)):
			return False
		elif (pNode_self.data != pNode_other.data):
			return False
		else:
			return self.is_similar_helper(pNode_self.left, pNode_other.left) and self.is_similar_helper(pNode_self.right, pNode_other.right) 

	def print_level (self, level):
		nodes = []
		self.print_level_helper(level, 1, nodes, self.root)
		if (len(nodes) == 0):
			return
		else:
			print(nodes)

	def print_level_helper (self, level, current_level, nodes, pNode):
		if (current_level > level or pNode == None):
			return
		if (current_level == level):
			nodes.append(pNode.data)
		else:
			self.print_level_helper(level, current_level + 1, nodes, pNode.left)
			self.print_level_helper(level, current_level + 1, nodes, pNode.right)

	def get_height (self):
		heights = [0]
		self.get_height_helper(self.root, 0, heights)
		heights.sort()
		max = heights[-1]
		return max

	def get_height_helper (self, pNode, length, heights):
		if (pNode == None):
			heights.append(length)
		else:
			length += 1
			self.get_height_helper(pNode.left, length, heights)
			self.get_height_helper(pNode.right, length, heights)

	def num_nodes (self):
		nodes = self.num_nodes_helper(self.root)
		return nodes

	def num_nodes_helper (self, pNode):
		if (pNode == None):
			return 0
		else:
			return 1 + self.num_nodes_helper(pNode.left) + self.num_nodes_helper(pNode.right)

	def insert (self, val):
		new_node = Node(val)
		if (self.root == None):
			self.root = new_node
			return
		current = self.root
		parent = self.root
		while (current != None):
			parent = current 
			if (val < current.data):
				current = current.left
			else:
				current = current.right
		if (val < parent.data):
			parent.left = new_node
		else:
			parent.right = new_node


def main():

	# Create three trees - two are the same and the third is different
	binary_tree_1 = Tree()
	binary_tree_1.insert(50)
	binary_tree_1.insert(30)
	binary_tree_1.insert(70)
	binary_tree_1.insert(10)
	binary_tree_1.insert(40)
	binary_tree_1.insert(60)
	binary_tree_1.insert(80)
	binary_tree_1.insert(7)

	binary_tree_2 = Tree()
	binary_tree_2.insert(50)
	binary_tree_2.insert(30)
	binary_tree_2.insert(70)
	binary_tree_2.insert(10)
	binary_tree_2.insert(40)
	binary_tree_2.insert(60)
	binary_tree_2.insert(80)
	binary_tree_2.insert(7)

	binary_tree_3 = Tree()
	nums = random.randint(0, 20)
	for i in range(nums):
		binary_tree_3.insert(random.randint(1, 50))

	# testing method is_similar()
	print("Binary Tree 1 and 2 are similar. Binary Tree 3 is different.\n")
	print("Testing is_similar() with 1 and 2: %s" %("Pass" if binary_tree_1.is_similar(binary_tree_2) else "Fail"))
	print("Testing is_similar() with 2 and 3: %s" %("Pass" if binary_tree_2.is_similar(binary_tree_3) else "Fail"))	
	print()

	# print various tree levels
	print("The levels of Tree 1 are: ")
	for i in range(1, 5):
		binary_tree_1.print_level(i)
	print()

	print("The levels of Tree 3 are: ")
	for i in range(1, nums):
		binary_tree_3.print_level(i)
	print()

	# get the height of two different trees
	print("The height of Tree 1 is %s" %(binary_tree_1.get_height()))
	print("The height of Tree 3 is %s" %(binary_tree_3.get_height()))
	print()

	# get the number of nodes of two different trees
	print("Tree 1 has %s nodes" %(binary_tree_1.num_nodes()))
	print("Tree 3 has %s nodes" %(binary_tree_3.num_nodes()))
	print()


main()
