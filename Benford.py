#  File: Benford.py

#  Description: Provind Benford's Law

#  Student Name: Hussain Bharmal

#  Student UT EID: hab889

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 11/29/1996

#  Date Last Modified: 11/29/1996

def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()

  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]
    pop_key = pop_num[0]
    pop_freq[pop_key] += 1

  # close the file
  in_file.close()
  
  #calculate relative frequencies
  rel_freq = []
  values = list(pop_freq.values())
  for i in range(len(pop_freq)):
    rel_freq.append((values[i]/sum(values))*100)
  
  # write out the result
  print("Digit\tCount\t%")
  for i in range(1,len(pop_freq)+1):
    value = i - 1
    key = str(i)
    print("%s\t%s\t%.1f" %(key,pop_freq[key],rel_freq[value]))
  
  
  
main()