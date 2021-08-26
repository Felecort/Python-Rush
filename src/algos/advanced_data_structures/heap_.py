# Почти полное бинарное дерево - всё заполненно, кроме
# последнего уровня

# Структура данных, основанная на бинарном дереве
# min heap - Сыновья деревьев больше, чем родитель
# max heap - Сыновья деревьев меньше, чем родитель
# push, pop - O(log(n))
# top - O(1)

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


heap = [None]
add(heap, 2)
add(heap, 5)
add(heap, 3)
add(heap, 10)
add(heap, 6)
add(heap, 9)
add(heap, 5)
add(heap, 12)
add(heap, 40)

print(top(heap))
pop(heap)
print(top(heap))
pop(heap)
print(top(heap))
pop(heap)
print(top(heap))
pop(heap)
print(top(heap))
pop(heap)
print(top(heap))
pop(heap)
print(top(heap))
pop(heap)
print(top(heap))
pop(heap)
print(top(heap))

