from random import randrange


def add(heap, x):  # O(log(n))
    heap.append(x)
    ind = len(heap) - 1
    while ind != 1 and heap[ind] < heap[ind // 2]:
        heap[ind], heap[ind // 2] = heap[ind // 2], heap[ind]
        ind //= 2


def pop(heap):  # O(log(n))
    heap[1],  heap[-1] =  heap[-1],  heap[1]
    heap.pop()
    ind = 1
    while ind * 2 < len(heap) and heap[ind] > heap[ind * 2] or\
            ind * 2 + 1 < len(heap) and heap[ind] > heap[ind * 2 + 1]:
        if ind * 2 + 1 >= len(heap) or heap[ind * 2] < heap[ind * 2 + 1]:
            heap[ind], heap[ind * 2] = heap[ind * 2], heap[ind]
            ind *= 2
        else:
            heap[ind], heap[ind * 2 + 1] = heap[ind * 2 + 1], heap[ind]
            ind += ind + 1


def top(heap):  # O(1)
    return heap[1]


def heap_sort(arr):
    heap = [None]
    for i in arr:
        add(heap, i)
    arr.clear()
    while len(heap) - 1:
        arr.append(top(heap))
        pop(heap)


for _ in range(100):
    arr = [randrange(0, 10000) for _ in range(1000)]
    sr_arr = sorted(arr)
    heap_sort(arr)
    print(sr_arr == arr)
