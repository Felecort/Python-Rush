from random import randrange


def counting_sort(arr):  # O(n + k) memory: O(n)
    minimum = arr[0]
    maximum = arr[0]
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
        if arr[i] < minimum:
            minimum = arr[i]
    bucket = [0 for _ in range(maximum - minimum + 1)]
    for i in range(len(arr)):
        bucket[arr[i] - minimum] += 1
    arr.clear()
    for i in range(len(bucket)):
        count = bucket[i]
        for j in range(count):
            arr.append(i + minimum)


arr = [randrange(50, 70) for _ in range(50)]
sr_arr = sorted(arr)
counting_sort(arr)
print(sr_arr == arr)
