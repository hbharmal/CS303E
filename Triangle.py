import time

#  File: Triangle.py

#  Description: Comparing searching algorithms

#  Student's Name: Hussain Bharmal

#  Student's UT EID: hab889

#  Date Created: 03/09/2018

#  Date Last Modified: 02/09/2018

# exaustive search
def exhaustive_search (grid):
	paths = find_path(grid)
	n = len(grid)
	max = 0
	for path in paths:
		path_sum = 0
		for i in range(n):
			x = grid[i][path[i]]
			path_sum += x
		if (path_sum > max):
			max = path_sum
	return max

# helper function for exuastive search 
def find_path(grid):
	n = len(grid)
	paths = [[0]]
	for i in range(1, n + 1):
		new_paths = []
		for path in paths:
			j = path[-1]
			new_path_a = path[:]
			new_path_b = path[:]
			new_path_a.append(j)
			new_path_b.append(j + 1)
			new_paths.append(new_path_a)
			new_paths.append(new_path_b)
		paths = new_paths
	return paths 

# greedy search
def greedy (grid):
	return grid[0][0] + greedy_helper(grid, 1, 0)

def greedy_helper (grid, i, j):
	if (i >= len(grid)):
		return 0
	else:
		if (grid[i][j] >= grid[i][j + 1]):
			return grid[i][j] + greedy_helper(grid, i + 1, j)
		else:
			return grid[i][j + 1] + greedy_helper(grid, i + 1, j + 1)

# recursive search
def rec_search (grid, i = 0, j = 0):
	num_rows = len(grid)
	if (i >= num_rows):
		return 0
	else:
		left = rec_search(grid, i + 1, j)
		right = rec_search(grid, i + 1, j + 1)
		final = max(left, right) + grid[i][j]
	return final

# dynamic programming
def dynamic_prog (grid):
	num_lines = len(grid)
	for i in range(num_lines - 2, -1, -1):
		for j in range(i + 1):
			grid[i][j] += max(grid[i + 1][j], grid[i + 1][j + 1])
	return grid[0][0]

def main ():
	# read triangular grid from file
	in_file = open("triangle1.txt", "r")
	num_lines = int(in_file.readline().strip())
	triangle = []
	for i in range(num_lines):
			row = in_file.readline().strip().split()
			for i in range(len(row)):
					row[i] = int(row[i])
			triangle.append(row)

	
	# exaustive approach
	ti = time.time()
	exaustive_total = exhaustive_search(triangle)
	tf = time.time()
	del_t = tf - ti
	print("The greatest path sum through exhaustive search is %s." %(exaustive_total))
	print("The time taken for exaustive search is %0.3E seconds." %(del_t))
	print()
	
	# greedy approach
	ti = time.time()
	greedy_total = greedy(triangle)
	tf = time.time()
	del_t = tf - ti
	print("The greatest path sum through greedy search is %s." %(greedy_total))
	print("The time taken for greedy approach is %0.3E seconds." %(del_t)) 
	print() 
	
	# recursive approach
	ti = time.time()
	rec_total = rec_search(triangle)
	tf = time.time()
	del_t = tf - ti
	print("The greatest path sum through recursive search is %s." %(rec_total))
	print("The time taken for recursive search is %0.3E seconds." %(del_t))
	print() 

	# dynamic programming
	ti = time.time()
	dynamic_total = dynamic_prog(triangle)
	tf = time.time()
	del_t = tf - ti
	# print time taken using dynamic programming
	print("The greatest path sum through dynamic programming is %s." %(rec_total))
	print("The time taken for dynamic programming is %0.3E seconds." %(del_t)) 
	print()

	print(triangle)

if __name__ == "__main__":
	main()