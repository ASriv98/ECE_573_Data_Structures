from __future__ import absolute_import

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pytest
import math
import random
import time
import numpy as np
from leftrb.llrb import LeftRB, is_red, is_black

from leftrb.bst import BinarySearchTree
import leftrb.llrb
trials = 1000

def path_calculation(root, curr_depth=0):
	
	if not root:
		return 0
	
	else:
		return curr_depth + path_calculation(root.left, curr_depth + 1) + path_calculation(root.right, curr_depth + 1)

def bst_test():
	global trials
	shuffle = BinarySearchTree()
	sort = BinarySearchTree()


	length_list = [10,100,200,300,400,500,600,700,800,900,1000]

	for length in length_list:
		shuffle_values = []
		sorted_values = []

		for i in range(trials):
			shuffled_numbers = list(range(length))
			sorted_numbers = shuffled_numbers.copy()
			random.shuffle(shuffled_numbers)
			
			for num in sorted_numbers:
				shuffle.insert(num,num)

			for num in shuffled_numbers:
				sort.insert(num,num)


			shuffle_length = path_calculation(shuffle.root)
			sort_length = path_calculation(sort.root)

			shuffle_values.append(shuffle_length/length)
			sorted_values.append(sort_length/length)

			
		
		print("shuffled", length, np.mean(shuffle_values))
		print("sorted", length, np.mean(sorted_values))

def variance(a, n): 
  
    # Compute mean (average of 
    # elements) 
    sum = 0
    for i in range(0 ,n): 
        sum += a[i] 
    mean = sum /n 
  
    # Compute sum squared  
    # differences with mean. 
    sqDiff = 0
    for i in range(0 ,n): 
        sqDiff += ((a[i] - mean)  
                * (a[i] - mean)) 
    return 0.01 * sqDiff / n 
  

def llrb_test():
	global trials
	shuffle = LeftRB()
	sort = LeftRB()
	average = []
	std_dev = []

	for length in range(10,10000,100):
		values = []
		
		for i in range(0,10):
			shuffle = LeftRB()

			shuffle_values = []

			shuffled_numbers = list(range(length))
			#sorted_numbers = shuffled_numbers.copy()
			random.shuffle(shuffled_numbers)
			#print("list: ",shuffled_numbers)

				#random.shuffle(shuffled_numbers)

			#for num in sorted_numbers:
			#	sort.insert(num,num)

			for num in shuffled_numbers:
				shuffle.insert(num,num)


			shuffle_length = path_calculation(shuffle.root)
			#print("length:",shuffle_length)

			values.append(shuffle_length/length)
			#print(values)

		#print("SV",values)
		temp_avg = np.mean(values)
		std_dev = math.sqrt(variance(values, len(values)))

		with open('data.csv', 'w') as f:

			writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

			writer.writerow([length, temp_avg, std_dev])

		print(length,',', temp_avg, ',',std_dev)
		#print("sorted", length, np.mean(sorted_values))

#llrb_test()
#bst_test()