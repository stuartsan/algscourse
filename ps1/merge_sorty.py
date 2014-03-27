# Implement merge sort as it will be required for inversion count

lst1 = [44, 12, 12414, 133, 8493, 11, 99]

def merge(lst1, lst2):
	i = 0
	j = 0
	output = []

	while i < len(lst1) and j < len(lst2):

		if lst1[i] < lst2[j]:
			output.append(lst1[i])
			i += 1
		else:
			output.append(lst2[j])
			j += 1

	return output + lst1[i:] + lst2[j:]

# Recursively divide and "conquer" the original list
def merge_sort(lst):
	
	if len(lst) <= 1:
		return lst

	else:
		mid = len(lst) / 2
		first_half = lst[:mid]
		second_half = lst[mid:]
		return merge(merge_sort(first_half), merge_sort(second_half))

def tests():
	lst = [3, 2, 1]
	lst = merge_sort(lst)
	assert lst == [1, 2, 3], 'Should sort a small list with no problemo'
	lst = [25, 14, 11, 1, 123]
	lst = merge_sort(lst)
	assert lst == [1, 11, 14, 25, 123], 'Should sort a bigger list with no problemo, too'
	lst = [1, 5, 2, 6, 2]
	lst = merge_sort(lst)
	assert lst == [1, 2, 2, 5, 6], 'Should sort a list with duplicate numbers'

if __name__ == '__main__':
	tests()