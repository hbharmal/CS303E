'''
  File: MagicSquare.py

  Description: Make a magic square

  Student's Name: Hussain Bharmal

  Student's UT EID: hab889
 
  Partner's Name: N/A

  Partner's UT EID: N/A

  Course Name: CS 313E 

  Unique Number: 51340

  Date Created: 01/23/2018

  Date Last Modified: 01/23/2018

'''

def make_square(n):
  matrix = [[0 for i in range(n)] for j in range(n)]
  
  #Intializing the first value of the matrix
  mid = n // 2;
  i = n-1
  j = mid
  matrix[i][j] = 1;
  
  #Constructing the rest of the matrix
  for k in range(2, n**2 + 1):
    if ((i < n-1 and j < n-1 and matrix[i+1][j+1] != 0) or (i == n-1 and j == n-1)):
      i -= 1 
    else:
      i += 1
      j += 1 
    
    #Reset row to 0 to wrap around borders
    if i > n-1:
      i = 0
    
    #Reset column to 0 to wrap around borders
    if j > n-1:
      j = 0
    
    matrix[i][j] = k
    
  return matrix
  
#Function to print the square in proper format
def print_square(magic_square):
  for i in range(len(magic_square[0])):
    for j in range(len(magic_square[0])):
      print("%-3s" %(magic_square[i][j]), end = "")
    print()
  print()

#Function to check if the matrix is a magic square
def check_square(magic_square):
  n = len(magic_square[0])
  sum = n * (n**2 + 1) / 2
  same = True;
  
  #Checking rows
  for i in range(n):
    sum_rows = 0
    for j in range(n):
      sum_rows += magic_square[i][j]
    if sum_rows != sum:
      same = False;
  
  #Checking columns
  for j in range(n):
    sum_columns = 0;
    for i in range(n):
      sum_columns += magic_square[i][j]
    if sum_columns != sum:
      same = False;
  
  #Checking for diagonal UL to LR 
  sum_diagonal1 = 0
  for i in range(n):
    sum_diagonal1 += magic_square[i][i]
  if sum_diagonal1 != sum:
    same = False;
  
  #Checking for diagonal LL to UR
  sum_diagonal2 = 0
  j = 0
  for i in range(n-1, -1, -1):
    sum_diagonal2 += magic_square[i][j]
    j += 1 
  if sum_diagonal2 != sum:
    same = False;
  
  if same != True:
    print("Matrix is not a magic square!")
  else:
    print("Sum of row = %d" %(sum))
    print("Sum of column = %d" %(sum))
    print("Sum diagonal (UL to LR) = %d" %(sum))
    print("Sum diagonal (UR to LL) = %d" %(sum))
    
  
def main():
  
  n = int(input("Please enter an add number: "))
  while (n < 3):
    n = int(input("Please enter an odd number: "))
  print()
  
  magic_square = make_square(n)
  
  print("Here is a %d by %d magic square" %(n, n))
  print_square(magic_square)
  
  check_square(magic_square)

main()
