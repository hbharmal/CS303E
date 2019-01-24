#  File: TopoSort.py

#  Description: Graph assignment 2

#  Student Name: Hussain Bharmal

#  Student UT EID: hab889

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 05/04/2018

#  Date Last Modified: 05/04/2018

class Stack (object):
	def __init__ (self):
		self.stack = []

	# add an item to the top of the stack
	def push (self, item):
		self.stack.append ( item )

	# remove an item from the top of the stack
	def pop (self):
		return self.stack.pop()

	# check what item is on top of the stack without removing it
	def peek (self):
		return self.stack[len(self.stack) - 1]

	# check if a stack is empty
	def isEmpty (self):
		return (len(self.stack) == 0)

	# return the number of elements in the stack
	def size (self):
		return (len(self.stack))

class Queue (object):
	def __init__ (self):
		self.queue = []

	def enqueue (self, item):
		self.queue.append (item)

	def dequeue (self):
		return (self.queue.pop(0))

	def isEmpty (self):
		return (len (self.queue) == 0)

	def size (self):
		return len (self.queue)

class Vertex (object):
	def __init__ (self, label):
		self.label = label
		self.visited = False

	# determine if a vertex was visited
	def wasVisited (self):
		return self.visited

	# determine the label of the vertex
	def getLabel (self):
		return self.label

	# string representation of the vertex
	def __str__ (self):
		return str (self.label)



class Graph (object):
	def __init__ (self):
		self.Vertices = []
		self.adjMat = []

	# check if a vertex already exists in the graph
	def hasVertex (self, label):
		nVert = len (self.Vertices)
		for i in range (nVert):
			if (label == (self.Vertices[i]).label):
				return True
		return False 

	# given a label get the index of a vertex
	def getIndex (self, label):
		nVert = len (self.Vertices)
		for i in range (nVert):
			if ((self.Vertices[i]).label == label):
				return i
		return -1

	# add a Vertex with a given label to the graph
	def addVertex (self, label):
		if not self.hasVertex (label):
			self.Vertices.append (Vertex(label))

		# add a new column in the adjacency matrix for the new Vertex
		nVert = len(self.Vertices)
		for i in range (nVert - 1):
			(self.adjMat[i]).append (0)
	  
		# add a new row for the new Vertex in the adjacency matrix
		newRow = []
		for i in range (nVert):
			newRow.append (0)
		self.adjMat.append (newRow)

	# add weighted directed edge to graph
	def addDirectedEdge (self, start, finish, weight = 1):
		self.adjMat[start][finish] = weight

	# add weighted undirected edge to graph
	def addUndirectedEdge (self, start, finish, weight = 1):
		self.adjMat[start][finish] = weight
		self.adjMat[finish][start] = weight

	def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
		fromVertexIndex = self.getIndex(fromVertexLabel)
		toVertexIndex = self.getIndex(toVertexLabel)
		if (fromVertexIndex == -1 or toVertexIndex == -1):
			return -1
		else:
			return self.adjMat[fromVertexLabel][toVertexLabel]

	# return an unvisited vertex adjacent to vertex v
	def getAdjUnvisitedVertex (self, v):
		nVert = len (self.Vertices)
		for i in range (nVert):
			if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
				return i
		return -1

	def getNeighbours (self, vertexLabel):
		vertexIndex = self.getIndex(vertexLabel)
		if (vertexIndex == -1):
			return -1
		l = []
		neighbours = self.adjMat[vertexIndex]
		for i in range(len(neighbours)):
			if (neighbours[i] > 0):
				l.append(i)
		return l 

	def getVertices (self):
		return self.Vertices

	def deleteEdge(self, fromVertexLabel, toVertexLabel):
		fromVertexIndex = self.getIndex(fromVertexLabel)
		toVertexIndex = self.getIndex(toVertexLabel)
		if (fromVertexIndex == -1 or toVertexIndex == -1):
			return -1
		else:
			self.adjMat[fromVertexIndex][toVertexIndex] = 0

	def deleteVertex (self, vertexLabel):
		vertexIndex = self.getIndex(vertexLabel)
		if (vertexIndex == -1):
			return -1
		# delete vertex
		del self.Vertices[vertexIndex]
		# delete all adges
		for i in range(len(self.adjMat)):
			del self.adjMat[i][vertexIndex]
		del self.adjMat[vertexIndex]

	# do the depth first search in a graph
	def dfs (self, v):
		# create a Stack
		theStack = Stack()

		# mark vertex v as visited and push on the stack
		(self.Vertices[v]).visited = True
		print (self.Vertices [v])
		theStack.push (v)

		# vist other vertices according to depth
		while (not theStack.isEmpty()):
			# get an adjacent unvisited vertex
			u = self.getAdjUnvisitedVertex (theStack.peek())
			if (u == -1): 
				u = theStack.pop()
			else:
				(self.Vertices[u]).visited = True
				print (self.Vertices[u])
				theStack.push(u)
		# the stack is empty let us reset the falgs
		nVert = len (self.Vertices)
		for i in range (nVert):
			(self.Vertices[i]).visited = False

	# do breadth first search in a graph
	def bfs (self, v):
		# create a Queue
		theQueue = Queue ()
		self.Vertices[v].visited = True
		print(self.Vertices[v])
		theQueue.enqueue(v)

		while (not theQueue.isEmpty()):
			vertex = theQueue.dequeue()
			neighbours = self.adjMat[vertex]

			for i in range(len(neighbours)):
				if ((not self.Vertices[i].wasVisited()) and (neighbours[i] > 0)):
					self.Vertices[i].visited = True
					print(self.Vertices[i])
					theQueue.enqueue(i)

		for i in range(len(self.Vertices)):
			self.Vertices[i].visited = False

	def hasCycle (self):
		for v in self.Vertices: 
			if self.hasCycleHelper(None, v):
				return True
		for i in range (len(self.Vertices)):
			(self.Vertices[i]).visited = False
		return False

	def hasCycleHelper(self, previous, v):
		if v.visited == True:
			return True
		v.visited = True
		neighbors = self.getNeighbors(v.label)
		if previous in neighbors:
			neighbors.remove(previous)
		if len(neighbors) == 0:
			return False
		for neighbor in neighbors:
			return self.hasCycleHelper(v, neighbor)

	def toposort (self):
		nVerts = len(self.Vertices)
		copyGraph = Graph()
		for v in self.Vertices:
		  copyGraph.addVertex(v.label)
		for i in range(nVerts):
		  for j in range(nVerts):
			copyGraph.addDirectedEdge(i, j, self.adjMat[i][j])  
		sorted = []
		if self.hasCycle():
		  return sorted
		while nVerts > 0:    
		  	row = 0
		  	while row < nVerts:
				for j in range(nVerts):
				  	if (copyGraph.adjMat[row][j] != 0):
						row += 1
						break
					if j == nVerts - 1:
				  		lastVert = copyGraph.Vertices[row]
				  		sorted.insert(0, lastVert)
				  		copyGraph.deleteVertex(lastVert.label)
				  		break
			nVerts -= 1      
	return sorted


def main():

	in_file = open("topo.txt", "r")
	v = int(in_file.readline().strip())
	theGraph = Graph()
	for i in range(v):
		vertex = in_file.readline().strip()
		theGraph.addVertex(vertex)
	e = int(in_file.readline().strip())
	for i in range(e):
		fromV, toV = input.readline().strip().split()
		theGraph.addDirectedEdge(fromV, toV)
	in_file.close()


main()



