from __future__ import absolute_import

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import math
import random
import numpy as np
from leftrb.llrb import LeftRB, is_red, is_black

from leftrb.bst import BinarySearchTree
import leftrb.llrb
trials = 10


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


def llrb_test():
	global trials
	shuffle = LeftRB()
	sort = LeftRB()


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

#llrb_test()
#bst_test()