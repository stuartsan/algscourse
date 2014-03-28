import sys

def two_sum(lst, targets):
    lookup = set(lst)
    yes_count = 0
    for target in targets:
        for num in lookup:
            if target - num is not num and target - num in lookup:
                yes_count += 1
                break
    return yes_count

def tests():
    lst = [4, 7, 1, 3, 19]
    targets = [11, 92]
    assert two_sum(lst, targets) == 1, 'Should identify one target match'
    targets = [11, 92, 8]
    assert two_sum(lst, targets) == 2, 'Should identify >1 target matches'
    lst = [5, 5]
    targets = [10, 92]
    assert two_sum(lst, targets) == 0, 'Should require distinct 2-summed nums'
    lst = [6, -4]
    targets = [2, 92]
    assert two_sum(lst, targets) == 1, 'Should work on neg. 2-summed nums'

def main():
    with open(sys.argv[1], 'r') as f:
        lines = [ int(line) for line in f.readlines() ]
    print two_sum(lines, range(-10000, 10000)) # outputs 427

if __name__ == '__main__':
    # main()
    tests()