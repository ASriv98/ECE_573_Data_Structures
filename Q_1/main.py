#read in text files and call to three sum 
import Three_sum
import os
import glob

current_dir = os.getcwd()

data_dir = os.listdir('hw1-1.data')
os.chdir('hw1-1.data')
result = Three_sum.three_sum()

#test_list = [-1,2,-3,4,5,6,7,8,9,10]
#result.Three_sum_with_bsearch(test_list, 26)


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

		#result.naive(input_list, 0)
		#result.Three_sum_with_bsearch(input_list, 0)
		result.sum3_with_hash_table(input_list, 0)






