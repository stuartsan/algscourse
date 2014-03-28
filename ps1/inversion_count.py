import sys

def sort_and_count(lst):
    """Basically divide and conquer merge sort."""
    if len(lst) <= 1:
        return (lst, 0)
    else:
        mid = len(lst) / 2
        first_half = lst[:mid]
        second_half = lst[mid:]
        return merge_and_count_inv(sort_and_count(first_half), 
                                   sort_and_count(second_half))

def merge_and_count_inv((lst1, count1), (lst2, count2)):
    """
    Recombine elements in sorted order. Also keep track of the number of 
    inversions, i.e., element pairs out of order.
    """
    i = 0
    j = 0
    count = 0
    output = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            output.append(lst1[i])
            i += 1
        else:
            output.append(lst2[j])
            j += 1
            count += len(lst1[i:])
    return (output + lst1[i:] + lst2[j:], count + count1 + count2)

def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    data = [int(line) for line in lines] # convert each line data to integer
    (_, count) = sort_and_count(data)    
    print count

if __name__ == '__main__':
    main()