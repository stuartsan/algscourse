# test_quick_sort.py
# David Prager Branner
# 20140327

import quick_sort as Q
import random

def test_quicksort_01():
    k = 10000
    rand_list = [random.randint(-k, k) for i in xrange(k)]
    copy_of_list = rand_list[:]
    Q.quick_sort(rand_list)
    assert rand_list == sorted(copy_of_list)

def test_quicksort_02():
    k = 10000
    rand_list = [random.randint(-k, k) for i in xrange(k)]
    copy_of_list = rand_list[:]
    Q.quick_sort(rand_list, pivot_mode='last')
    assert rand_list == sorted(copy_of_list)

def test_quicksort_03():
    k = 10000
    rand_list = [random.randint(-k, k) for i in xrange(k)]
    copy_of_list = rand_list[:]
    Q.quick_sort(rand_list, pivot_mode='best_of_three')
    assert rand_list == sorted(copy_of_list)

def test_find_median_01():
    k = 1000
    for i in xrange(k):
        rand_list = [random.randint(-k, k) for i in range(3)]
        true_middle = sorted(rand_list)[1]
        assert true_middle == Q.find_median(*rand_list)
