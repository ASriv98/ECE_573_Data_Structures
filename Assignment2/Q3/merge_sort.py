def MergeSort(argShuffledList):
	comparison_count = 0

	if len(argShuffledList) > 1:
		intMidValue = len(argShuffledList)//2
		listLeftHalf = argShuffledList[:intMidValue]
		listRightHalf = argShuffledList[intMidValue:]

		left_part = MergeSort(listLeftHalf)
		right_part = MergeSort(listRightHalf)

		comparison_count += left_part[1] + right_part[1]

		i=0
		j=0
		k=0
		while i < len(listLeftHalf) and j < len(listRightHalf):
			comparison_count += 1
			if listLeftHalf[i] < listRightHalf[j]:
				argShuffledList[k]=listLeftHalf[i]
				i =i+1

			else:
				argShuffledList[k]=listRightHalf[j]
				j=j+1

			k=k+1

		while i < len(listLeftHalf):
			argShuffledList[k]=listLeftHalf[i]
			i=i+1
			k=k+1
			comparison_count += 1

		while j < len(listRightHalf):
			argShuffledList[k]=listRightHalf[j]
			j=j+1
			k=k+1
			comparison_count += 1

	return argShuffledList, comparison_count/2
count = 0

def merge(left, right):
	global count

	result = []
	x, y = 0, 0
	for z in range(0, len(left) + len(right)):
		if x == len(left): # if at the end of 1st half,
			result.append(right[y]) # add all values of 2nd half
			y+=1
		elif y == len(right): # if at the end of 2nd half,
			result.append(left[x]) # add all values of 1st half
			x+=1
		elif right[y] < left[x]:
			count+=1
			result.append(right[y])
			y+=1
		else:
			count+=1
			result.append(left[x])
			x+=1
	return result


def bottomup_mergesort(list):
	global count
	count = 0

	length = len(list)
	size = 1
	while size < length:
		size+=size # initializes at 2 as described
		for pos in range(0, length, size):
			sublist_start = pos
			sublist_mid   = pos + (size / 2)
			sublist_end = pos + size
			left  = list[ sublist_start : sublist_mid ]
			right = list[   sublist_mid : sublist_end ]
			list[sublist_start:sublist_end] = merge(left, right)
	return list, count