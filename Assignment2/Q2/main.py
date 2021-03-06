#read in text files and call to three sum 
import os
import glob
import kendallTau
import time

current_dir = os.getcwd()

data_dir = os.listdir('hw2-2.data')
os.chdir('hw2-2.data')

for x in range(0,1):

	for file in data_dir:
		input_list = []
		print(file)		#check current file we are reading
		
		f = open(file, "r")
		file_by_line = f.readlines()		
		
		for x in file_by_line:
			input_list.append(x.strip())		#adding values from text file into an array

		input_list = list(map(int, input_list))	#converting string to an integer 

		start_time = time.time()
		sorted_list, inversion_count = kendallTau.mergeSortInversions(input_list)
		print(inversion_count)
		elapsed_time = time.time() - start_time
		print(elapsed_time)


