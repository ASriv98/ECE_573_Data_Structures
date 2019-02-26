#read in text files and call to three sum 
import os
import glob
import quick_sort	
import merge_sort
import shellsort
import bucket_sort
import time


input_list = []
print(file)		#check current file we are reading
		
f = open('hw3.data', "r")
file_by_line = f.readlines()		
		
for x in file_by_line:
	input_list.append(x.strip())		#adding values from text file into an array

input_list = list(map(int, input_list))	#converting string to an integer 
input_list2 = input_list
input_list3 = input_list
input_list4 = input_list


#start_time = time.time()
#quick_sort.quickSort(input_list)
#elapsed_time = time.time() - start_time

start_time = time.time()
result, c = merge_sort.MergeSort(input_list2)
elapsed_time = time.time() - start_time
print(elapsed_time)

start_time = time.time()
shellsort.shellsort(input_list3, [1])
elapsed_time = time.time() - start_time
print(elapsed_time)

start_time = time.time()
bucket_sort.bucket_sort(input_list4)
elapsed_time = time.time() - start_time
print(elapsed_time)


