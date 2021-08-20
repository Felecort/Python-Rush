from random import randrange

def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            return True
        if arr[m] < x:
            l = m + 1
        elif arr[m] > x:
            r = m - 1
    return False



arr = [x for x in range(20)]
print(binary_search(arr, 7))
