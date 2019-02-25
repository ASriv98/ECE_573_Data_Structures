# Python program for implementation of MergeSort 
global total_count

def merge_sort_top_down(arr, comparison_count): 

	if len(arr) > 1: 
		mid = len(arr)//2 #Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements  
		R = arr[mid:] # into 2 halves 
  
		total_count += merge_sort_top_down(L) # Sorting the first half 
		total_count += merge_sort_top_down(R) # Sorting the second half 
  
		i = j = k = 0
		  		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				comparison_count+=1
				arr[k] = L[i] 
				i+=1
			else: 
				comparison_count+=1
				arr[k] = R[j] 
				j+=1
			k+=1
		  
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		  
		while j < len(R): 
			arr[k] = R[j] 
			j+=1
			k+=1


