#read in text files and call to three sum 
import max_difference
import os
import glob

current_dir = os.getcwd()

data_dir = os.listdir('hw1-4.data')
os.chdir('hw1-4.data')


for x in range(0,10):

	for file in data_dir:
		input_list = []
		print(file)		#check current file we are reading
		
		f = open(file, "r")
		file_by_line = f.readlines()		
		
		for x in file_by_line:
			input_list.append(x.strip())		#adding values from text file into an array

		input_list = list(map(float, input_list))	#converting string to an integer 

		max_difference.max_difference(input_list)





