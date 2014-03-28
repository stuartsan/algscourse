import sys

# this count is needed basically to test that you implemented quicksort right
bad_global_count = 0 

def quick_sort(items, left=None, right=None, pivot_mode='first'):
    """Sorts things, ties the room together."""
    global bad_global_count
    if left == None:
        left = 0
    if right == None:
        right = len(items) - 1
    bad_global_count += right - left
    choose_pivot_idx(items, left, right, pivot_mode)
    newIndex = partition(items, left, right)
    if newIndex - left > 1: quick_sort(items, left, newIndex - 1, pivot_mode)
    if right - newIndex > 1: quick_sort(items, newIndex + 1, right, pivot_mode)

def partition(items, left, right):
    """
    Accepts list and left/right indexes to work within.
    Partitions sublist around value of leftmost item.
    """
    pivot, i = items[left], left + 1
    # j == index dividing looked at / not yet looked at
    for j in range(left + 1, right + 1):
        if items[j] < pivot:
            items[j], items[i] = items[i], items[j] # swap
            i += 1
    items[left], items[i-1] = items[i-1], items[left] # swap
    return i -1

def choose_pivot_idx(items, left=None, right=None, mode='first'):
    """Swaps an item into the left position to be used as pivot."""
    if left == None:
        left == 0
    if right == None:
        right = len(items) - 1
    # By default, mode = 'first'
    if mode == 'last':
        items[left], items[right] = items[right], items[left]
    # Compare the first, last, and middle elements.
    # Whichever is median, use as pivot to create a more balanced recursive
    # split.
    elif mode == 'best_of_three':
        length, first, last = right - left, items[left], items[right]
        if not length % 2:
            middleIdx = (left + right) / 2
        else:
            middleIdx = ((left + right) / 2) - 1
        middle = items[middleIdx]
        median = find_median(first, middle, last)
        # Swap median into the first position; default: median = first
        if median is last:
            items[left], items[right] = items[right], items[left]
        elif median is middle:
            items[left], items[middleIdx] = items[middleIdx], items[left]

def find_median(first, middle, last):
    """Determine median."""
    templist = [first, middle, last]
    templist.remove(max(templist))
    templist.remove(min(templist))
    return templist[0]

def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    items = [int(line) for line in lines]
    quick_sort(items)
    print bad_global_count

if __name__ == '__main__':
    main()