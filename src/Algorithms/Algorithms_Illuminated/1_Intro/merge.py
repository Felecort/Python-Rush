
from random import randint


def merge(arr1, arr2):
    res = []
    i_arr1 = 0
    i_arr2 = 0

    for _ in range(len(arr1) + len(arr2)):

        if i_arr1 >= len(arr1):
            return res + arr2[i_arr2:]
        if i_arr2 >= len(arr2):
            return res + arr1[i_arr1:]

        if arr1[i_arr1] >= arr2[i_arr2]:
            res.append(arr2[i_arr2])
            i_arr2 += 1
        else:
            res.append(arr1[i_arr1])
            i_arr1 += 1
    return res


if __name__ == "__main__":
    arr1 = sorted([randint(0, 10) for _ in range(7)])
    arr2 = sorted([randint(0, 10) for _ in range(7)])
    print(arr1)
    print(arr2)
    arr = merge(arr1, arr2)
    print(arr)
