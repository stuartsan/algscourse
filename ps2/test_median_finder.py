"""Test two simple ways of finding the median of a three-element list."""

import random

def m():
    """Test whether min(max(list)) returns the median. (It does not.)"""
    while True:
        k = 1000
        lst = [random.randint(-k, k) for i in range(3)]
        if sorted(lst)[1] != min(max(lst[0:2]), lst[2]):
            break
    print lst, sorted(lst)[1], min(max(lst[0:2]), lst[2])

def n():
    """Test whether popping min() and max() returns the median. (It does.)"""
    while True:
        k = 1000
        lst = [random.randint(-k, k) for i in range(3)]
        lst2 = lst[:]
        lst.remove(max(lst))
        lst.remove(min(lst))
        if lst != [sorted(lst2)[1]]:
            break
    print lst, [sorted(lst2)[1]]
