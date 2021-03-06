import time 

def optimized(list, target_sum):
	print("in optimized")
	count = 0

	start_time = time.time()

	list.sort()	#sorting takes log(n) time complexity
					#lookup python default sorting method 
	for i in range(0, len(list) - 2):

		front_index = i + 1;
		back_index = len(list) - 1;

		while (front_index < back_index):

			if (list[i] + list[front_index] + list[back_index] == target_sum):
				print(list[i],list[front_index],list[back_index])
				print("Target sum was found!")
				print(list[i],list[j],list[k])
				return

			elif (list[i] + list[front_index] + list[back_index] < target_sum):
				count += 1
				front_index += 1

			else:
				back_index -= 1

	elapsed_time = time.time() - start_time
	print("Total time taken: ", elapsed_time)


def sum3_with_hash_table(list, target_sum):
	start_time = time.time()
	print('in n^2')

	result = []
	n = len(list)
	hashmap = {}
	for i in range(n):
		hashmap[list[i]] = 1
	list.sort()                          # O(N log N)

        # Python ranges exclude the last term, i.e., range(0,3) = [0,1,2]
	for i in range(0, n-2):           # for i = 0 to N-3
		for j in range(i+1, n-1):       # for j = i+1 to N-2
			search_value = -(list[i] + list[j])
			if list[i] < list[j] < search_value and search_value in hashmap:
				result.append( [list[i], list[j], search_value] )

	elapsed_time = time.time() - start_time
	print("Total time taken: ", elapsed_time)
	return result

	
