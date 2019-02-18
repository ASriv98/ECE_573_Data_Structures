import time 


def max_difference(list):
	max_i, min_i = 0, 0
	start_time = time.time()


	# iterate the list from the second index
	for i in range(1, len(list)):
	    if list[i] > list[max_i]:
	        max_i = i

	    if list[i] < list[min_i]:
	        min_i = i

	distance = list[max_i] - list[min_i]

	elapsed_time = time.time() - start_time
	print(list[min_i], list[max_i], distance) 
	print("the total time taken is: ", elapsed_time)