#  File: TestLinkedList.py

#  Description: Linked List assignment

#  Student Name: Hussain Bharmal

#  Student UT EID: hab889

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 03/39/2018

#  Date Last Modified: 03/29/2018

class Link (object):
	def __init__(self, item, next = None):
		self.item = item
		self.next = next
	
	def __str__(self):
	  return str(self.item)

class LinkedList (object):

	# constructor 
	def __init__(self):
		self.first = None

	# get number of links 
	def get_num_links (self):
		count = 0
		current = self.first
		while (current.next != None):
			count += 1
			current = current.next
		return count
	
	# add an item at the beginning of the list
	def insert_first (self, item): 
		newFirst = Link(item)
		newFirst.next = self.first
		self.first = newFirst

	# add an item at the end of a list
	def insert_last (self, item): 
		newLast = Link(item)
		current = self.first
		if (current == None):
		  self.first = newLast
		  return
		while (current.next != None):
			current = current.next
		current.next = newLast

	# add an item in an ordered list in ascending order
	def insert_in_order (self, item): 
		if (self.first == None):
			self.insert_first(item)
			return
		elif (item < self.first.item):
			self.insert_first(item)
			return
		else:
			newLink = Link(item)
			current = self.first
			previous = self.first
			while (item > current.item):
				if (current.next == None):
					self.insert_last(item)
					return
				else:
					previous = current 
					current = current.next
			previous.next = newLink
			newLink.next = current

	# search in an unordered list, return None if not found
	def find_unordered (self, item): 
		current = self.first
		if (current == None):
			return None
		while (current != None):
			if (current.item == item):
				return current
			else:
				current = current.next
		return None

	# Search in an ordered list, return None if not found
	def find_ordered (self, item): 
		current = self.first
		if (current == None):
			return None
		while (current.next != None):
			if (current.item == item):
				return current
			elif (item < current.item):
				return None
			else:
				current = current.next
		return None


	# Delete and return Link from an unordered list or None if not found
	def delete_link (self, item):
		current = self.first
		previous = self.first
		if (current == None):
			return None
		while (current.next != None):
			if (current.item == item):
				if (current == self.first):
					self.first = self.first.next
				else:
					previous.next = current.next
				return current
			else:
				previous = current
				current = current.next
		return None

	# String representation of data 10 items to a line, 2 spaces between data
	def __str__ (self):
		text = ""
		current = self.first
		iter = 1
		if (self.is_empty()):
			return "LinkedList is Empty"
		while (current.next != None):
			if (iter % 10 == 0):
				text += "\n"
				text += str(current.item) + "  "
			else:
				text += str(current.item) + "  "
			iter += 1
			current = current.next
		return text

	# Copy the contents of a list and return new list
	def copy_list (self):
		clone = LinkedList()
		current = self.first
		while (current != None):
			clone.insert_last(current.item)
			current = current.next
		return clone

	# Reverse the contents of a list and return new list
	def reverse_list (self): 
		clone = LinkedList()
		current = self.first
		while (current != None):
			clone.insert_first(current.item)
			current = current.next
		return clone

	# Sort the contents of a list in ascending order and return new list
	def sort_list (self): 
		sorted_list = LinkedList()
		current = self.first
		if (self.is_empty()):
			return sorted_list
		while (current != None):
			sorted_list.insert_in_order(current.item)
			current = current.next
		return sorted_list

	# Return True if a list is sorted in ascending order or False otherwise
	def is_sorted (self):
		current = self.first
		if (self.is_empty() or self.get_num_links() == 1):
			return True
		while (current != None):
			if (current.item > current.next.item):
				return False
			current = current.next
		return True

	# Return True if a list is empty or False otherwise
	def is_empty (self): 
		return (self.first == None)

	# Merge two sorted lists and return new list in ascending order
	def merge_list (self, other):
		new_list = LinkedList()
		current = self.first
		while current.next != None:
			new_list.insert_in_order(current.item)
			current = current.next
		current = other.first
		while current.next != None:
			new_list.insert_in_order(current.item)
			current = current.next
		return new_list

	# Test if two lists are equal, item by item and return True
	def is_equal (self, other):
		if (self.get_num_links() != other.get_num_links()):
			return False
		if (self.is_empty() and other.is_empty()):
			return True
		current_1 = self.first
		current_2 = other.first
		while (current_1.next != None):
			if (current_1.item != current_2.item):
				return False
			current_1 = current_1.next
			current_2 = current_2.next
		return True

	# Return a new list, keeping only the first occurence of an element
	# and removing all duplicates. Do not change the order of the elements.
	def remove_duplicates (self):
		new_list = self.copy_list()
		previous = new_list.first
		current = new_list.first
		elements = []
		while (current.next != None):
			if (current.item in elements):
				previous.next = current.next
			else:
				elements.append(current.item)
				previous = current
			current = current.next
		return new_list

def main():
	test_case = [1, 2, 5, 9, 4, 8, 7]
	
	# Test methods insert_first() and __str__() by adding more than 10 items to a list and printing it.
	print("Testing methods insert_first() & __str__().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_first(test_case[i])
	print(test_list)
	del test_list
	print()

	# Test method insert_last()
	print("Testing method insert_last().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_last(test_case[i])
	print(test_list)
	del test_list
	print()

	# Test method insert_in_order()
	print("Testing method insert_in_order().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_in_order(test_case[i])
	print(test_list)
	del test_list
	print()

	# Test method get_num_links()
	print("Testing method get_num_links().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_first(test_case[i])
	print("List: %s" %(test_list))
	print("Result: %s" %(test_list.get_num_links()))
	del test_list
	print()

	# Test method find_unordered() 
	# Consider two cases - item is there, item is not there 
	print("Testing method find_unordered().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_first(test_case[i])
	print("Find 9: %s" %(test_list.find_unordered(9)))
	print("Find 3: %s" %(test_list.find_unordered(3)))
	del test_list
	print()

	# Test method find_ordered() 
	# Consider two cases - item is there, item is not there
	print("Testing method find_ordered().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_in_order(test_case[i])
	print("Find 9: %s" %(test_list.find_ordered(9)))
	print("Find 3: %s" %(test_list.find_ordered(3)))
	del test_list
	print()

	# Test method delete_link()
	# Consider two cases - item is there, item is not there 
	print("Testing method delete().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_first(test_case[i])
	print("Delete 9: %s" %(test_list.delete_link(9)))
	print("Delete 3: %s" %(test_list.delete_link(3)))
	del test_list
	print()

	# Test method copy_list()
	print("Testing method copy_list().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_last(test_case[i])
	test_list_copy = test_list.copy_list()
	print("Initial List: %s" %(test_list))
	print("Copy List: %s" %(test_list_copy))
	del test_list
	print()

	# Test method reverse_list()
	print("Testing method reverse_list().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_last(test_case[i])
	test_list_reverse = test_list.reverse_list()
	print("Initial List: %s" %(test_list))
	print("Reverse List: %s" %(test_list_reverse))
	del test_list
	print()

	# Test method sort_list()
	print("Testing method sort_list().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_last(test_case[i])
	test_list_sorted = test_list.sort_list()
	print("Initial List: %s" %(test_list))
	print("Sorted List: %s" %(test_list_sorted))
	del test_list
	print()

	# Test method is_sorted()
	# Consider two cases - list is sorted, list is not sorted
	print("Testing method is_sorted().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_last(test_case[i])
	test_list_sorted = test_list.sort_list()
	print("Initial List: %s" %(test_list))
	print("Sorted List: %s" %(test_list_sorted))
	del test_list
	print()

	# Test method is_empty()
	print("Testing method is_empty().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_last(test_case[i])
	print("Current List: %s" %(test_list))
	print("Result: %s" %(test_list.is_empty()))
	del test_list
	print()

	# Test method merge_list()
	print("Testing method merge_list().")
	test_list = LinkedList()
	test_list_2 = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_last(test_case[i])
		test_list_2.insert_first(test_case[i])
	merged_list = test_list.merge_list(test_list_2)
	print("Initial List: %s" %(test_list))
	print("Merged List: %s" %(merged_list))
	del test_list, test_list_2
	print()

	# Test method is_equal()
	# Consider two cases - lists are equal, lists are not equal
	print("Testing method is_equal().")
	test_list = LinkedList()
	test_list_2 = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_in_order(test_case[i])
		test_list_2.insert_first(test_case[i])
	print("List 1: %s" %(test_list))
	print("List 2: %s" %(test_list_2))
	print("Result: %s" %(test_list.is_equal(test_list_2)))
	test_list_3 = test_list_2.sort_list()
	print("List 1: %s" %(test_list))
	print("List 2: %s" %(test_list_3))
	print("Result: %s" %(test_list.is_equal(test_list_3)))  
	del test_list, test_list_2, test_list_3
	print()

	# Test remove_duplicates()
	print("Testing method remove_duplicates().")
	test_list = LinkedList()
	for i in range (len(test_case)):
		test_list.insert_in_order(test_case[i])
	test_list.insert_in_order(4)
	test_list.insert_in_order(8)
	removed = test_list.remove_duplicates()
	print("List with duplicates: %s" %(test_list))
	print("List without duplicates: %s" %(removed))
	del test_list, removed
	print()

if __name__ == "__main__":
	main()