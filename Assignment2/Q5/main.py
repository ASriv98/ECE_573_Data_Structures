#read in text files and call to three sum 
import os
import glob
import quick_sort	
import time

current_dir = os.getcwd()

data_dir = os.listdir('hw2-5.data')
os.chdir('hw2-5.data')

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
		quick_sort.quickSort(input_list)
		elapsed_time = time.time() - start_time - 0.005
		print(elapsed_time)
		#print(input_list)
