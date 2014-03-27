from random import randint as get_random_int

def random_select(items, left, right, order):
	"""
	Takes an unsorted list and finds the item of an order stastic (e.g., 4th element if
	the list were in order) in linear time.
	"""
	
	length = right - left

	if not items:
		return items
	elif length == 0:
		return items[left]

	# Pick a random pivot index
	random_idx = get_random_int(left, right)

	# Swap the pivot into the left position to call partition
	items[left], items[random_idx] = items[random_idx], items[left]

	# Partition, get the randomly chosen item's new index
	partition_idx = partition(items, left, right)
	
	if partition_idx == order:
		return items[partition_idx]
	elif partition_idx > order:
		return random_select(items, left, partition_idx - 1, order)
	elif partition_idx < order:
		return random_select(items, partition_idx + 1, length - partition_idx, order - partition_idx)


def partition(items, left, right):
	"""
	Accepts array and left/right indexes to work within.
	"""
	pivot = items[left]
	i = left + 1     		# index within the partition dividing less than / greater than pivot element

	for j in range(left + 1, right + 1):  # j == index dividing looked at / not yet looked at
		if items[j] < pivot:
			items[j], items[i] = items[i], items[j] # swap
			i += 1
		
	items[left], items[i-1] = items[i-1], items[left]     # swap
	return i - 1


def tests():
	assert(random_select([], 0, 1, 1) == []), "Should just return list if one or no elements"
	lst = [8, 2, 1, 3]
	assert random_select(lst, 0, len(lst)-1, 0) == 1, 'Should identify first element'
	lst = [8, 2, 1, 3]
	assert random_select(lst, 0, len(lst)-1, 1) == 2, 'Should identify second element'
	lst = [3,2,1,0]
	assert random_select(lst, 0, len(lst)-1, 3) == 3, 'Should identify last element'


if __name__ == '__main__':
	tests()