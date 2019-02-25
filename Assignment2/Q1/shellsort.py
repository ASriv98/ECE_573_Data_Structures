import math
import time

def shellsort(list, gap_list):
	length = len(list)
	gap_list_length = len(gap_list)
	#print(gap_list_length)
	comparison_count = 0
	comparison_count_unsorted = 0

	gap = gap_list[0]
	x = 1

	while gap > 0:

		for i in range(gap, length):

			temp = list[i]
			j = i

			comparison_count_unsorted += 1		#count for the sorted data set
			while j >= gap and list[j - gap] > temp:
				comparison_count += 1
				list[j] = list[j - gap]
				j -= gap

			list[j] = temp
		
		if x <= (gap_list_length - 1):
			gap = gap_list[x]
		
		else:
			gap = -10

		x += 1

	print("amount of comparisons inside sort loop",comparison_count)
	print("total number of comparisons",comparison_count_unsorted+comparison_count)

