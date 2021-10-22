
def find_set(v):
    if v == parents[v]:
        return v
    parents[v] = find_set(parents[v])
    return parents[v]


def union_set(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if sizes[a] < sizes[b]:
            a, b = b, a
        parents[b] = a
        sizes[a] += sizes[b]


sizes = [1] * 10
parents = [i for i in range(10)]

print(find_set(0))
print(find_set(1))
union_set(0, 1)
print(find_set(0))
print(find_set(1))
union_set(1, 2)
union_set(2, 3)
union_set(2, 4)
union_set(4, 5)
print(find_set(1))
print(find_set(2))
print(find_set(3))
print(find_set(4))
print(find_set(5))
print(find_set(6))