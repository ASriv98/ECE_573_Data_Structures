#read in text files and call to three sum 
import os
import glob
import quick_algs
import time 



current_dir = os.getcwd()

data_dir = os.listdir('hw1-2.data')
os.chdir('hw1-2.data')
input_list = []
n = 8192


for x in range(0,1):

	for file in data_dir:
		input_list = []
		print(file)		#check current file we are reading
		
		f = open(file, "r")
		file_by_line = f.readlines()		
		
		for x in file_by_line:
			p,q = x.split()
			p = int(p)
			q = int(q)
			input_list.append([p,q])


		#quick find algorithm 
		start_time = time.time()
		part_1 = quick_algs.QuickFind(n)

		for i in range(0, len(input_list)):
			if not part_1.find(input_list[i][0], input_list[i][1]):
				part_1.union(input_list[i][0], input_list[i][1])

		elapsed_time = time.time() - start_time
		print("Total time taken: ", elapsed_time)


		#quick union algorithm
		start_time = time.time()
		part_2 = quick_algs.QuickUnion(n)

		for i in range(0, len(input_list)):
			if not part_2.find(input_list[i][0], input_list[i][1]):
				part_2.union(input_list[i][0], input_list[i][1])

		elapsed_time = time.time() - start_time
		print("Total time taken: ", elapsed_time)


		#weighted quick union algorithm
		start_time = time.time()
		part_3 = quick_algs.WeightedQuickUnion(n)

		for i in range(0, len(input_list)):
			if not part_3.find(input_list[i][0], input_list[i][1]):
				part_3.union(input_list[i][0], input_list[i][1])

		elapsed_time = time.time() - start_time
		print("Total time taken: ", elapsed_time)
