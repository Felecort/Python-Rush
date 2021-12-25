
def max_sum(a, ranges):
    pref_sum = [0, a[0]]
    pfer_sum_add = pref_sum.append
    amounts = set()
    amounts_add = amounts.add

    for i in range(1, len(a)):
        pfer_sum_add(pref_sum[i] + a[i])
        # pref_sum.append(pref_sum[i] + a[i])

    for left, right in ranges:
        amounts_add(pref_sum[right + 1] - pref_sum[left])
        # amounts.add(pref_sum[right + 1] - pref_sum[left])
    return max(amounts)


print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1], [(1, 3), (0, 4), (6, 8)]))
