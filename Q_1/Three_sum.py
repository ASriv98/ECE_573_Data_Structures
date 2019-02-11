#!/usr/bin/python
import time

class three_sum():


	def naive(self, list, target_sum):
		print("in naive")
		count = 0

		start_time = time.time()

		for i in range(0, len(list) - 2):
			for j in range(i+1, len(list) - 1):
				for k in range(j+1, len(list)):

					if (list[i] + list[j] + list[k] != target_sum):
						count+=1

					elif (list[i] + list[j] + list[k] == target_sum):
						elapsed_time = time.time() - start_time
						print(list[i],list[j],list[k])
						print("Target sum was found!")
						print("Total time taken: ", elapsed_time)
						print("Total number of comparisons: ", count)
						return

	def optimized(self, list, target_sum):
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
					elapsed_time = time.time() - start_time
					print(list[i],list[front_index],list[back_index])
					print("Target sum was found!")
					print("Total time taken: ", elapsed_time)
					print("Total number of comparisons: ", count)
					return

				elif (list[i] + list[front_index] + list[back_index] < target_sum):
					count += 1
					front_index += 1

				else:
					back_index -= 1

		print("Target sum does not exist")








