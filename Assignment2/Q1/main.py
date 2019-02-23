#read in text files and call to three sum 
import Three_sum
import os
import glob

current_dir = os.getcwd()

data_dir = os.listdir('hw1-1.data')
os.chdir('hw1-1.data')
result = Three_sum.three_sum()


for x in range(0,5):

	for file in data_dir:
		input_list = []
		print(file)		#check current file we are reading
		
		f = open(file, "r")
		file_by_line = f.readlines()		
		
		for x in file_by_line:
			input_list.append(x.strip())		#adding values from text file into an array

		input_list = list(map(int, input_list))	#converting string to an integer 
		#print(input_list)


		#naive is O(n^3) implementation
		#Three_sum_with_bsearch uses binary search and is n^2log(n) implementation
		result.naive(input_list, 0)
		result.Three_sum_with_bsearch(input_list, 0)

		#naive does not finish on large data sets of 4096 and above for about 30 minutes and above






