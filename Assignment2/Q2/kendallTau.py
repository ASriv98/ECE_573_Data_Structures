#!/usr/bin/env python
import os, sys

def mergeSortInversions(list):
	if len(list) == 1:
		return list, 0
   
	else:
		#split the array into left half and right half 
		left = list[:len(list)/2]
		right = list[len(list)/2:]


		left, left_count = mergeSortInversions(left)
		right, right_count = mergeSortInversions(right)
		sorted_list = []
		i = 0
		j = 0
		inversions = 0 + left_count + right_count
	
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			sorted_list.append(left[i])
			i += 1
		else:
			sorted_list.append(right[j])
			j += 1
			inversions += (len(left)-i)
	sorted_list += left[i:]
	sorted_list += right[j:]


	return sorted_list, inversions