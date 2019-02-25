#read in text files and call to three sum 
import os
import glob
import shellsort

current_dir = os.getcwd()

data_dir = os.listdir('hw2-1.data')
os.chdir('hw2-1.data')
gap_list = [7,3,1]
gap_list_insertion_sort = [1]


for x in range(0,1):

	for file in data_dir:
		input_list = []
		print(file)		#check current file we are reading
		
		f = open(file, "r")
		file_by_line = f.readlines()		
		
		for x in file_by_line:
			input_list.append(x.strip())		#adding values from text file into an array

		#print(input_list)
		input_list = list(map(int, input_list))	#converting string to an integer 


		shellsort.shellsort(input_list, gap_list)
		#shellsort.shellsort(input_list, gap_list_insertion_sort)




