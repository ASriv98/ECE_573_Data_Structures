#!/usr/bin/python
import time

def binary_search(a, key):
	lo, hi = 0, len(a)-1
	while (lo <= hi):
		mid = lo + (hi-lo)/2
		if key < a[mid]:    
			hi = mid - 1
		elif key > a[mid]:  
			lo = mid + 1
		else:               
			return mid


	return None



class three_sum():


	def naive(self, list, target_sum):
		print("in n^3")
		count = 0

		start_time = time.time()

		for i in range(0, len(list) - 2):
			for j in range(i+1, len(list) - 1):
				for k in range(j+1, len(list)):

					if (list[i] + list[j] + list[k] == target_sum):
						print("Target sum was found!")
						print(list[i],list[j],list[k])
						return




		elapsed_time = time.time() - start_time
		print("Total time taken: ", elapsed_time)

	def Three_sum_with_bsearch(self, list, target_sum):
		print("in n^2logn")
		start_time = time.time()
		n = len(list)
		result = 0
  		list.sort()        #python sorts in n log n time                   

		for i in range(0, len(list)): 
			for j in range(i+1, len(list)):       
				search_value = -(list[i] + list[j])
				valid_index = binary_search(list, search_value)
				if (valid_index > j):
					result+=1


		print(result) #result represents if we found a sum = to 0 or not 
		elapsed_time = time.time() - start_time
		print("Total time taken: ", elapsed_time)
		return result



	#def sum3_with_hash_table(self,a):
	#	start_time = time.time()
	#	print('in n^2')

	#	res = []
	#	N = len(a)
	#	d = {}
	#	for i in range(N):
	#		d[a[i]] = 1
	#		a.sort()                          # O(N log N)

	        # Python ranges exclude the last term, i.e., range(0,3) = [0,1,2]
	#	for i in range(0, N-2):           # for i = 0 to N-3
	#		for j in range(i+1, N-1):       # for j = i+1 to N-2
	#			val = -(a[i] + a[j])
	#			if a[i] < a[j] < val and val in d:
	#				res.append( [a[i], a[j], val] )

	#	elapsed_time = time.time() - start_time
	#	print("Total time taken: ", elapsed_time)
	#	return res

		











