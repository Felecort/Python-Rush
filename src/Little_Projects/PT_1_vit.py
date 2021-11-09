import random


def is_learn_books_near():
    arr = [0, 0, 0, 1, 1, 1, 1]
    random.shuffle(arr)
    for i in range(4):
        row = 0
        for j in range(1, 4):
            if arr[i] == arr[i + j]:
                row += 1
            if row == 3:
                # print("True: ", arr)
                return True
    # print("False: ", arr)
    return False


def probability_4_books_near():
    counter = 0
    for i in range(1_000_000):
        if is_learn_books_near():
            counter += 1
    print(counter / i)


probability_4_books_near()