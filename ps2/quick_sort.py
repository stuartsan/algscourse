import sys

bad_global_count = 0 # this count is needed basically to test that you implemented quicksort right so whatevs

def quick_sort(items, left, right, pivot_mode='first'):
	"""
	Sorts things, ties the room together.
	"""
	global bad_global_count
	bad_global_count += right - left

	choose_pivot_idx(items, left, right, pivot_mode)
	newIndex = partition(items, left, right)
	
	if newIndex - left > 1: quick_sort(items, left, newIndex - 1, pivot_mode)
	if right - newIndex > 1: quick_sort(items, newIndex + 1, right, pivot_mode)

def partition(items, left, right):
	"""
	Accepts list and left/right indexes to work within. Partitions sublist around value of leftmost item.
	"""
	pivot, i = items[left], left + 1

	for j in range(left + 1, right + 1):  # j == index dividing looked at / not yet looked at
		if items[j] < pivot:
			items[j], items[i] = items[i], items[j] # swap
			i += 1
		
	items[left], items[i-1] = items[i-1], items[left] # swap
	return i -1

def choose_pivot_idx(items, left, right, mode):
	"""
	Swaps an item into the left position to be used as pivot 
	"""
	if mode == 'first': pass

	elif mode == 'last': items[left], items[right] = items[right], items[left]

	# Compare the first, last, and middle elements. Whichever is median, use as pivot
	# to create a more balanced recursive split
	elif mode == 'best_of_three':
		
		length, first, last = right - left, items[left], items[right]
		middleIdx = (left + right) / 2 if not length % 2 else ((left + right) / 2) - 1
		middle = items[middleIdx]
		
		# Determine median
		sort_me = [first, last, middle]
		sort_me.sort()
		median = sort_me[1]

		# Swap median into the first position

		if median is first: pass  # Just chill
		
		elif median is last: 
			items[left], items[right] = items[right], items[left]
		
		elif median is middle: 
			items[left], items[middleIdx] = items[middleIdx], items[left]

def tests():
	lst = [3, 2, 1]
	quick_sort(lst, 0, len(lst)-1)
	assert lst == [1,2,3], 'Should sort a small list with no problemo'
	lst = [25, 14, 11, 1, 123]
	quick_sort(lst, 0, len(lst)-1)
	assert lst == [1, 11, 14, 25, 123], 'Should sort a bigger list with no problemo, too'
	lst = [1, 5, 2, 6, 2]
	quick_sort(lst, 0, len(lst)-1)
	assert lst == [1, 2, 2, 5, 6], 'Should sort a list with duplicate numbers'

def main():
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()
	items = [int(line) for line in lines]
	quick_sort(items, 0, len(items)-1)   
	print bad_global_count

if __name__ == '__main__':
	tests()
	# main()