class Link (object):

	# Constructor
	def __init__(self, data, next = None):
		self.data = data
		self.next = next


class CircularList (object):

	# Constructor
	def __init__(self):
		self.first = None
		self.num_links = 0

	def insert (self, item):
		if (self.first == None):
			self.first = Link(item)
			self.num_links += 1
		elif (self.first.next == None):
			self.last = Link(item)
			self.last.next = self.first
			self.num_links += 1
		else:
			newLast = Link(item)
			self.last.next = newLast
			newLast.next = self.first
			self.num_links += 1

	def find (self, key):
		if (self.first == None):
			return None
		elif (self.first.data == key):
			return self.first
		current = self.first.next
		while (current != self.first):
			if (current.data == key):
				return current
			current = current.next
		return None

		if (self.first == None):
			return None


	def delete (self, key):
		current = self.first
		previous = self.first

		if (current == None):
			return None

		while (previous.next != self.first):
			previous = previous.next

		while (current.data != key):
			if (current.next == self.first):
				return None
			else:
				previous = current
				current = current.next

		if (current == self.first):
			self.first = self.firt.next

		previous.next = current.next
		self.num_links -= 1

		return current


	def delete_after(self, start, n):
		current = self.find(start)
		previous = self.find(start)
		i = 1

		while (i < n):
			current = current.next
			previous = current
			i += 1

		if (current == self.first):
			self.first = self.first.next

		previous.next = current.next
		self.num_links -= 1

		return current.next

	def __str__(self):
		text = ""
		current = self.first
		for i in range(self.num_links):
			text += str(self.first.data) + "  "
		return text


def main():
	in_file = open("josephus.txt", "r")
	soldiers = int(in_file.readline().strip())
	start = int(in_file.readline().strip())
	increment = int(in_file.readline().strip())
	group = CircularList()
	for i in range(1, soldiers + 1):
		group.insert(i)
	if (group.first != None):
		group.delete_after(start, increment)
	else:
		print(group)

main()













