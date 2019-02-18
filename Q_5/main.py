#read in text files and call to three sum 
import Three_sum
import os
import glob

current_dir = os.getcwd()

data_dir = os.listdir('hw1-5.data')
os.chdir('hw1-5.data')



for x in range(0,5):

	for file in data_dir:
		input_list = []
		print(file)		#check current file we are reading
		
		f = open('8192int.txt', "r")
		file_by_line = f.readlines()		
		
		for x in file_by_line:
			input_list.append(x.strip())		#adding values from text file into an array

		#print(input_list)
		input_list = list(map(int, input_list))	#converting string to an integer 
		#print(input_list)

		Three_sum.sum3_with_hash_table(input_list)
		Three_sum.optimized(input_list,0)


