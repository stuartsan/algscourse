def binary_search(lst, elem, left, right):
	"""
	Operates recursively on a single list by manipulating left/right/middle indexes
	"""
	if right - left <= 0:
		return left if lst and lst[left] == elem else -1

	mid = (left + right) / 2
	
	if lst[mid] == elem:
		return mid

	elif lst[mid] > elem:
		new_right = mid - 1
		return binary_search(lst, elem, left, new_right)

	elif lst[mid] < elem:
		new_left = mid + 1
		return binary_search(lst, elem, new_left, right)

def tests():
	haystack = [1]
	needle = 1
	assert binary_search(haystack, needle, 0, len(haystack) - 1) == 0, 'Should find item when list length is 1'
	haystack.append(3)
	assert binary_search(haystack, needle, 0, len(haystack) - 1) == 0, 'Should find item when list length is 2'
	haystack = [1,3,5,7]
	needle = 7
	assert binary_search(haystack, needle, 0, len(haystack) - 1) == 3, 'Should find item when list length even'
	haystack.append(9)
	assert binary_search(haystack, needle, 0, len(haystack) - 1) == 3, 'Should find item when list length odd'
	needle = 99
	assert binary_search(haystack, needle, 0, len(haystack) - 1) == -1, 'Should return -1 if item not found'
	haystack = []
	assert binary_search(haystack, needle, 0, len(haystack) - 1) == -1, 'Should return -1 if list length is 0'

if __name__ == '__main__':
	tests()