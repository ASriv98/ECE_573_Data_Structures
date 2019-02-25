
class MergeSort:

	def __init__(self):
		self.count = 0

	def top_down(self,list):
		start = 0;
		end = len(list) - 1

		temp = list
		self.count = 0

		self.sort(list, temp, start, end)
		print("kendall tau distance", self.count)

	def sort(self,list, temp, start, end):
		if (end - start <= 0):
			return

		#print(list, temp, start, end)
		mid = start + (end-start)/2
		self.sort(temp, list, start, mid)
		self.sort(temp, list, mid +1, end)
		self.merge(list, temp, start, mid, end)

		#print(list)

	def merge(self,list, temp, start, mid, end):
		left = start
		right = mid + 1 
	
		for i in range(start, end+1):

			if (left > mid):
				list[i] = temp[right]
				right = right + 1
			elif (right > end):
				list[i] = temp[left]
				left = left + 1 

			elif (temp[left] <= temp[right]):
				list[i] = temp[left]
				left = left + 1
			else:
				self.count = self.count + mid - left + 1
				list[i] = temp[right]
				right = right + 1 

		#print(list)
		


# Python program for implementation of MergeSort 
def mergeSort(arr): 


	if len(arr) > 1: 
		mid = len(arr)//2 #Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements  
		R = arr[mid:] # into 2 halves 
  
		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 
  
		i = j = k = 0
		  
		kendall_count = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+=1
			else: 
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


# Code to print the list 
#def printList(arr): 
#	for i in range(len(arr)):         
#		print(arr[i],end=" ") 
#	print() 