#  File: Boxes.py

#  Description: Largest subset of boxes problem

#  Student Name: Hussain Bharmal

#  Student UT EID: hab889

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 2/23/2018

#  Date Last Modified: 2/23/2018

# Find all subsets
def sub_sets (boxes, subsets, index, final):
  if (index == len(boxes)):
    box_sort(subsets, final)
  else:
    temp = subsets[:]
    subsets.append (boxes[index])
    sub_sets (boxes, temp, index + 1, final)
    sub_sets (boxes, subsets, index + 1, final)

# Sort the boxes such that they fit inside each other
def box_sort(box, final):
  stop = False
  for i in range(len(box) - 1):
      for j in range(3):
        if (box[i + 1][j] <= box[i][j]):
          stop = True
          break
  if (len(box) > 1 and stop == False):
    final.append(box)


def main():

  # dimensions of the box
  boxes = []
  # subsets of boxes
  subsets = []
  # boxes with subsets that fit inside each other
  final = []
  max = 0

  in_file = open("boxes.txt", "r")
  num_boxes = int(in_file.readline().strip())
  for i in range(num_boxes):
    box = in_file.readline().strip().split()
    for i in range(len(box)):
      box[i] = int(box[i]) 
    box.sort()
    boxes.append(box)
  
  in_file.close()

  # Sorts list in ascending order
  boxes.sort()
  sub_sets(boxes, subsets, 0, final)

  # Find max 
  max_list = []

  # Find the max
  for i in range(len(final)):
    if (len(final[i]) > max):
      max = len(final[i])

  # the list is from biggest to smallest, so invert it
  final = final[::-1]
  
  if (max < 2):
    print("No Nesting Boxes")
  else:
    print("Largest Subset of Nesting Boxes")
    for i in range(len(final)):
      if len(final[i]) == max:
        for j in range(len(final[i])):
          print(final[i][j])
        print()

main()