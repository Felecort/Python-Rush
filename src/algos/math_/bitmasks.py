
def bitmask(arr):
    n = len(arr)
    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                print(arr[i], end=" ")
        print()


arr = [1, 2, 77, 4]
bitmask(arr)
