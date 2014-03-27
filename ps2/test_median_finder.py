import random

def m():
    while True:
        k = 1000
        lst = [random.randint(-k, k) for i in range(3)]
        if sorted(lst)[1] != min(max(lst[0:2]), lst[2]):
            break
    print lst, sorted(lst)[1], min(max(lst[0:2]), lst[2])

def n():
    while True:
        k = 1000
        lst = [random.randint(-k, k) for i in range(3)]
        lst2 = lst[:]
        lst.remove(max(lst))
        lst.remove(min(lst))
        if lst != [sorted(lst2)[1]]:
            break
    print lst, [sorted(lst2)[1]]
