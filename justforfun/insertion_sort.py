def insertion_sort(lst):
	for j in range(1, len(lst)): #for each index in the list, starting with 1 (0 is sorted)
		key = lst[j]
		i = j - 1
		while i >= 0 and lst[i] > key:
			lst[i + 1] = lst[i]
			i = i - 1
		lst[i + 1] = key

def tests():
	lst = [3, 2, 1]
	insertion_sort(lst)
	assert lst == [1,2,3], 'Should sort a small list with no problemo'
	lst = [25, 14, 11, 1, 123]
	insertion_sort(lst)
	assert lst == [1, 11, 14, 25, 123], 'Should sort a bigger list with no problemo, too'
	lst = [1, 5, 2, 6, 2]
	insertion_sort(lst)
	assert lst == [1, 2, 2, 5, 6], 'Should sort a list with duplicate numbers'

if __name__ == '__main__':
	tests()
	