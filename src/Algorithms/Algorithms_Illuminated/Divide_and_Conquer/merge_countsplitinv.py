
def merge_and_count_inv(arr1, arr2):
    res = []
    i_arr1 = 0
    i_arr2 = 0
    split_counter = 0

    for _ in range(len(arr1) + len(arr2)):

        if i_arr1 >= len(arr1):
            return split_counter
        if i_arr2 >= len(arr2):
            return split_counter

        if arr1[i_arr1] >= arr2[i_arr2]:
            res.append(arr2[i_arr2])
            i_arr2 += 1
            split_counter += len(arr1[i_arr1:])
        else:
            res.append(arr1[i_arr1])
            i_arr1 += 1
    return split_counter


if __name__ == "__main__":
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    arr = merge_and_count_inv(arr1, arr2)
    print(arr)
