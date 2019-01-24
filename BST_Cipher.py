
#  File: BST_Cipher.py

#  Description: Encryption assignment

#  Student Name: Hussain Bharmal

#  Student UT EID: hab889

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 04/16/2018

#  Date Last Modified: 04/16/2018


class Node (object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Tree (object):
	# the init() function creates the binary search tree with the
	# encryption string. If the encryption string contains any
	# character other than the characters 'a' through 'z' or the
	# space character drop that character.
	def __init__ (self, encrypt_str):
		self.root = None
		for ch in encrypt_str:
			if ((ch >= 'a' and ch <= 'z') or ch == ' '):
				self.insert(ch)

	# the insert() function adds a node containing a character in
	# the binary search tree. If the character already exists, it
	# does not add that character. There are no duplicate characters
	# in the binary search tree.
	def insert (self, ch):
		new_node = Node(ch)
		if (self.root == None):
			self.root = new_node
			return
		current = self.root
		parent = self.root
		while (current != None):
			parent = current
			if (ch == ' '):
				current = current.left
			elif (ch > current.data):
				current = current.right 
			elif (ch < current.data):
				current = current.left 
			elif (ch == current.data):
				return
		if (ch > parent.data):
			parent.right = new_node
		else:
			parent.left = new_node

	# the search() function will search for a character in the binary
	# search tree and return a string containing a series of lefts
	# (<) and rights (>) needed to reach that character. It will
	# return a blank string if the character does not exist in the tree.
	# It will return * if the character is the root of the tree.
	def search (self, ch):
		if (ch == self.root.data):
			return "*"
		if (ch == ' '):
			cur = self.root
			txt = ""
			while (cur.left != None):
				cur = cur.left
				txt += "<"
			return txt 
		current = self.root
		text = ""
		while (current != None):
			if (ch > current.data):
				current = current.right
				text += ">"
			elif (ch < current.data):
				current = current.left
				text += "<"
			elif (ch == current.data):
				return text
		return ""


	# the traverse() function will take string composed of a series of
	# lefts (<) and rights (>) and return the corresponding 
	# character in the binary search tree. It will return an empty string
	# if the input parameter does not lead to a valid character in the tree.
	def traverse (self, st):
		current = self.root
		for i in range(len(st)):
			if (st[i] == "<" and current != None):
				current = current.left
			elif (st[i] == ">" and current != None):
				current = current.right
		if (current == None):
			return ""
		else:
			return current.data

	# the encrypt() function will take a string as input parameter, convert
	# it to lower case, and return the encrypted string. It will ignore
	# all digits, punctuation marks, and special characters.
	def encrypt (self, st):
		text = ""
		for ch in st:
			if ((ch >= 'a' and ch <= 'z') or ch == ' '):
				text += self.search(ch) + "!"
		return text[:-1]

	# the decrypt() function will take a string as input parameter, and
	# return the decrypted string.
	def decrypt (self, st):
		st = st.split("!")
		text = ""
		for token in st:
			text += self.traverse(token)
		return text

def main():

	# ask for encryption key
	key = input("Enter encryption key: ")

	# construct tree
	tree = Tree(key)

	# encrypted string
	str1 = input("Enter string to be encrypted: ")
	print(tree.encrypt(str1))

	# decrypted string
	str2 = input("Enter string to be decrypted: ")
	print(tree.decrypt(str2))


main()