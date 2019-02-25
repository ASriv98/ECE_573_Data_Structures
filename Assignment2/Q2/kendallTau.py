
class MergeSort:

	def __init__(self):
		self.count = 0

	def top_down(self,list):
		start = 0;
		end = len(list) - 1

		temp = list;

		self.sort(list, temp, start, end)
		print("kendall tau distance", self.count)

	def sort(self,list, temp, start, end):
		if (end - start <= 0):
			return

		mid = start + (end-start)/2
		self.sort(temp, list, start, mid)
		self.sort(temp, list, mid +1, end)
		self.merge(list, temp, start, mid, end)

	def merge(self,list, temp, start, mid, end):
		left = start
		right = mid + 1 
		for i in range(start, end):

			if (left > mid) and (right < len(list) + 1):
				list[i] = temp[right + 1]
			elif (right > end):
				list[i] = temp[left + 1]
			else:
				self.count = self.count + mid - left + 1
				if (right < len(list) + 1):
					list[i] = temp[right ]

	print(list)